# Maxim Dokalenko — Static Web App

Lightweight static web app with a small Python-based API (Azure Function) for sending email via Brevo (Sendinblue).

## Features
- Static frontend (HTML/CSS/JS)
- Azure Functions-based `sendEmail` endpoint (uses Brevo SDK)
- Example request helper script for local testing (`request.py`)
- Utility script(s) in `scripts/`

## Quick Start

Prerequisites
- Python 3.8+ and `pip`
- (Optional) Azure Functions Core Tools if you want to run the Function locally: https://learn.microsoft.com/azure/azure-functions/functions-run-local

Run the static site locally
```bash
# from repository root
python -m http.server 8000
# then open http://localhost:8000
```

Run the API (Azure Function) locally
```bash
cd api
pip install -r requirements.txt
# Ensure any required settings (see local.settings.json) are set, e.g. BREVO_API_KEY for the email provider
# Start the Functions host (requires Azure Functions Core Tools):
func start
```

Test the `sendEmail` endpoint
- `request.py` is a small example script that POSTs JSON to `http://localhost:7071/api/sendEmail` when the Functions host is running.

## Configuration
- `api/local.settings.json` contains local settings used by the Functions host. Do not commit production secrets.
- `api/sendEmail/email_provider.py` expects an environment variable `BREVO_API_KEY` (Brevo / Sendinblue API key).

## Files & Structure
- `_todo.txt` — project notes
- `index.html`, `index copy.html` — frontend pages
- `style.css` — main styles
- `request.py` — example POST to the local `sendEmail` function
- `api/` — Azure Functions project
  - `host.json`, `local.settings.json` — Functions host config
  - `requirements.txt` — Python dependencies for the Functions app
  - `sendEmail/` — function that forwards mail via `api/sendEmail/email_provider.py`
- `scripts/` — helper scripts (e.g. `generate_manifest.py`)
- `static/`, `fonts/`, `images/` — static assets

## Notes
- The `sendEmail` function uses Brevo (sib_api_v3_sdk). Ensure `BREVO_API_KEY` is available in the environment or in `local.settings.json` for local testing.
- There are no deployment scripts included for Azure Static Web Apps or Function App in this repo; `staticwebapp.config.json` hints at static web app hosting. Configure CI/CD (GitHub Actions, Azure) separately.

## Next steps / Suggestions
- Add a brief CONTRIBUTING or DEPLOYMENT section if you want automated deploys
- Add example env var templates (e.g. `.env.example`) and an Azure deployment guide if you plan to host in Azure

---
Generated documentation — edit to add project-specific details or credentials handling instructions.