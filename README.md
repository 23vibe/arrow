# 23 vibe open-source project

Aimed at promoting underground artists, DJs and producers of non-commercial music. Thanks to GitHub Inc, which is offering free hosting public repositories on GitHub pages. Should serve as an entry point / landing page - for linking all of your spread resources into one place. Like, music, fanpages, featured projects etc. Free webpage on free tier for free artists on fr23 vibe connectiong free people. 

The repo is a blueprint/template for a simple webpage with easy maintenance. The only requirement is to not upload content, that violates any law, mainly GDPR and copytights. Content owners must be ready o prove, that they have consent of any people shown on the photos with publication. It means if you have our friends on the photos with you, just ask them by email if they are ok with being on the photo with you on the webpage and keep the email archived. We have a private repo "GDPR", you can keep the items there. The consent should explicitly mention the filename or photo url. The same is valid for music. This does not apply for embedded items, such as SoundCloud and MixCloud players - the responsibility is on the platform's side.

## How does it work

index.html - the file containing code for the main page. Info section is dedicated for your introduction/bio and is not expected to change very often - so it is hardcoded. Short text inputs in the gallery are taken from `/static/info.txt` - commais the separator; one sentence = one field. Gallery is updated by adding/removing photo files to `/static/images/`, to take effect page have to be re-deployed (on push by the workflow). Contact form will be plugged soon. then you'll be able to contact not only for booking, but also if ya'd like to have such a page for you/your project. Want to contribute? If you are in our scope - you are welcome to show your skills!

## Maxim Dokalenko — Static Web App

Lightweight html/css static web page including javascripts for gallery displaying effects and contact form. Contact form points at external Python-based API (not yet) for sending email via Brevo. Credit for graphics and design goes to Different Engine, code, deployment and maintenance: Maxim Dokalenko (now you understand why I paused scratching for now heh).

## Features
- Static frontend (HTML/CSS/JS)
- External API-based `sendEmail` endpoint (uses Brevo SDK), curently structured as Azure Function App. To test locally, install Azure Functions Core Tools, configure environmental variables and run on localhost.
- Utility script(s) in `scripts/`

## Quick Start

Prerequisites
- Python 3.8+ and `pip`
- (Optional) Azure Functions Core Tools if you want to run the Function locally: https://learn.microsoft.com/azure/azure-functions/functions-run-local

Run the static site locally (for full scripts functionality)
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

## Configuration
- `api/local.settings.json` contains local settings used by the Functions host. Do not commit production secrets.
- `api/sendEmail/email_provider.py` expects an environment variable `BREVO_API_KEY` (Brevo / Sendinblue API key).

## Files & Structure
- `index.html` — frontend pages
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

---
Generated documentation — edit to add project-specific details or credentials handling instructions.

---

Cheers, 
I.S. aka M.D.