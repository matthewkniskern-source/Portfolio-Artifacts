# Enterprise Security Governance and Automation
Status: development baseline, not production or certified compliant.
A cloud-first, reproducible security engineering lab integrating infrastructure as code, CI security gates, evidence, and human governance. No physical lab or AWS credentials required for static checks.
## Start
Run `python -m unittest discover -s Enterprise-Security-Automation/tests -v` from repository root. Install Terraform and run `terraform -chdir=Enterprise-Security-Automation/infrastructure/aws init -backend=false`, then validate. Review the workflow under .github/workflows. No deployment workflow exists yet.
## Architecture
Change request -> static validation/scans -> evidence -> human decision -> future authorized deployment -> runtime evidence.
## Boundaries
Public portfolio: synthetic data only. Never commit secrets, state, real contract data or customer findings. AWS deployment, OIDC, actual branch protection, dashboard, runtime evidence and formal compliance assessment are future work. A passing check is not compliance certification.
See documentation/roadmap.md and governance/legacy-integration.md.
