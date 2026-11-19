"""Offline provisioning of NIST JSON schemas pinned to published release asset hashes."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

ASSET_SHA256 = {
    "1.2.2": {
        "catalog":"fdc559f5dff6848b1ebbe1898a69cc08263479f7c796e2f056412059e7489d0c",
        "profile":"04329bd68032f48825f712f79576b3fd00e129e59d3597beb56ed72c17277f66",
        "component":"3b6e0765c44037c4d1bfb2cdb972713917d3eca73e566c0e6c6881a565638830",
        "ssp":"d7f9bf67101829083472a8f058a5b5ef078e09b3f699ac0c4dbe33a5b0671b6a",
        "assessment-plan":"ba265f05982969142cbc3c6ed6bb99e0880081ceb366c152e44fe7e2b08aa125",
        "assessment-results":"d4e1e7e17c6662814882810ad64075266964ee1a575759ce3955302fd74edcd9",
        "poam":"c8f2ce52b3c71299bb0c9e1cd950d48dc79d9f52920c543ac30b3c3f08c2e152",
        "mapping":"45b4f909f72e17fbe8476e2a7f3d9f64ec42dc26ab2fe2d56c6b44fc57346022",
    },
    "1.2.3": {
        "catalog":"ab95836e9e8dfeb6fde80007f6cc76fa3192f595d427c751a3f3923c3f474fc2",
        "profile":"7c5ff5a92683b6a80ce6a3474dea04e0ea8680a4ecb60702ffa08ebfc677e6cb",
        "component":"95e76881151ececd5cb1a93ff0f70ad74b8cc1aa58771626ac8b262bf2c8e001",
        "ssp":"99b1bee2df5604a7d4f1faeab43148e0bd4c4a1f513cd0d2d0c7896aa216a1e7",
        "assessment-plan":"ea687b9d0ab1d84c9cb11ee0a5e22b17956fe892ee93f5acca937bef81d23ea2",
        "assessment-results":"4034e2032332dbf597e59e0646ec16c2c31df992962490371e91f47b219ff42c",
        "poam":"f4fd94487408a9589954b5b92d88965c984d4f79b85365cc574b860898759437",
        "mapping":"ed28b68c8e56cc7d39f0c6076a5d7da3e8100fbe25abf5bb731120bd34f8817e",
    },
}
RELEASE_SHA256 = {
    "1.2.2":"d2935239d3eac06cd65ed77295b92023bb3921e035755b89c87e7e42bd4b85a4",
    "1.2.3":"eefb4ec5b1383d3b15fca27e0b63bc84b8661d6ee17e4f92acb437606e9ee982",
}
TARGET = Path(__file__).resolve().parents[1]/"interoperability"/"oscal"/"schemas"
MAX_ASSET=4_000_000

def provision(source, version, target=TARGET):
    expected={"oscal_"+model+"_schema.json":sha for model,sha in ASSET_SHA256[version].items()}
    assets={}
    if source.is_dir():
        for name in expected:
            path=source/name
            if path.is_file():
                if path.stat().st_size>MAX_ASSET:
                    raise ValueError("Schema member exceeds limit")
                assets[name]=path.read_bytes()
    else:
        if source.stat().st_size>5_000_000 or hashlib.sha256(source.read_bytes()).hexdigest()!=RELEASE_SHA256[version]:
            raise ValueError("Release archive does not match published SHA-256")
        with ZipFile(source) as z:
            for item in z.infolist():
                name=Path(item.filename).name
                if name not in expected:
                    continue
                if name in assets or item.file_size>MAX_ASSET:
                    raise ValueError("Unexpected schema member")
                assets[name]=z.read(item)
    if not assets:
        raise ValueError("No supported schema files found; obtain individual release assets")
    for name,raw in assets.items():
        if hashlib.sha256(raw).hexdigest()!=expected[name]:
            raise ValueError("Schema asset fingerprint mismatch: "+name)
        json.loads(raw)
    folder=target/version
    folder.mkdir(parents=True,exist_ok=True)
    for name,raw in assets.items():
        (folder/name).write_bytes(raw)
    manifest={}
    for name,sha in expected.items():
        path=folder/name
        if path.is_file() and path.stat().st_size<=MAX_ASSET and hashlib.sha256(path.read_bytes()).hexdigest()==sha:
            manifest[name]=sha
    (folder/"schema-manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return sorted(manifest)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("source",type=Path,help="Directory of official JSON release assets or pinned release ZIP")
    parser.add_argument("--version",choices=ASSET_SHA256,default="1.2.3")
    args=parser.parse_args()
    print(provision(args.source,args.version))
