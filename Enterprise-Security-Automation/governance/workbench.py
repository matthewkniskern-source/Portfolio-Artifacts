"""Local-only browser interface. No authentication or persistence; synthetic data only."""
import json
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer
from requirements_engine import assess

ROOT=Path(__file__).resolve().parents[1]
PROFILE=ROOT/"governance"/"profiles"/"synthetic-project-a.json"
UI=ROOT/"dashboard"/"requirements.html"

class Handler(BaseHTTPRequestHandler):
    def send(self, data, kind="application/json", status=200):
        self.send_response(status)
        self.send_header("Content-Type",kind)
        self.send_header("Content-Length",str(len(data)))
        self.send_header("Cache-Control","no-store")
        self.send_header("X-Content-Type-Options","nosniff")
        self.send_header("Content-Security-Policy","default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(data)
    def do_GET(self):
        if self.path=="/":
            self.send(UI.read_bytes(),"text/html; charset=utf-8")
        elif self.path=="/profile":
            self.send(PROFILE.read_bytes())
        else:
            self.send(b'{"error":"Not found"}',status=404)
    def do_POST(self):
        if self.path!="/assess":
            self.send(b'{"error":"Not found"}',status=404)
            return
        if self.headers.get("Origin") not in (None,"http://127.0.0.1:8765"):
            self.send(b'{"error":"Invalid origin"}',status=403)
            return
        try:
            if self.headers.get_content_type()!="application/json":
                raise ValueError("JSON required")
            size=int(self.headers.get("Content-Length","0"))
            if not 0<size<=1_000_000:
                raise ValueError("Invalid request size")
            data=json.loads(self.rfile.read(size))
            result=assess(data["profile"],data.get("evidence"),data.get("scanned",[]))
            self.send(json.dumps(result).encode())
        except (ValueError,TypeError,KeyError,AttributeError) as exc:
            self.send(json.dumps({"error":str(exc)}).encode(),status=400)

if __name__=="__main__":
    print("Local synthetic requirements workbench: http://127.0.0.1:8765")
    HTTPServer(("127.0.0.1",8765),Handler).serve_forever()
