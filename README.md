# static-shop
Static web app template with product portfolio and function app integration.

🏗️ Architecture Overview
1. Static Web App (HTML + CSS)
Hosted on Azure Static Web Apps (or Azure Storage with static website hosting).
Contains your form (<form> with fields like name, email, message).
2. Azure Function App (API)
Exposed as an API endpoint (/api/sendEmail).
Triggered by HTTP POST from your form.
Uses an email service (e.g., SendGrid, SMTP, or Azure Communication Services) to send the email.

## Project structure
```
azure-static-form-email/
│
├── README.md
├── staticwebapp.config.json
├── index.html
├── style.css
├── .github/
│   └── workflows/
│       └── azure-static-web-apps.yml
└── api/
    ├── host.json
    ├── requirements.txt
    ├── local.settings.json         # for local dev only (not deployed - add to .gitignore)
    ├── sendEmail/
    │   ├── __init__.py
    │   └── function.json
    └── shared/
        └── email_provider.py

```
## Deployment
CI/CD pipeline for updates.

🔑 Setup Steps
Create Static Web App in Azure Portal → point it to your GitHub repo (or local build).
Add Function App inside the same Static Web App (Azure automatically wires /api/* routes).
Configure SendGrid (or another email provider):
Create a SendGrid resource in Azure Marketplace.
Get the API key.
Add it to your Function App’s Application Settings as SENDGRID_API_KEY.
Deploy → GitHub Actions or Azure DevOps pipeline will handle CI/CD.

# Generated markdown

# Static contact form + Azure Function email

A minimal Azure Static Web App with a simple HTML+CSS contact form and a Python Azure Function that sends emails via SendGrid.

## Prerequisites
- Azure subscription
- GitHub repository
- SendGrid account (or use Azure Marketplace SendGrid)
- Python 3.10+ for local function testing
- Azure Functions Core Tools for local run (optional)

## Quick start
1. **Fork/clone** this repo.
2. **Create Azure Static Web App** in Azure Portal.
   - App location: `/`
   - API location: `api`
   - Output location: `/` (no build)
3. **Configure application settings** in the SWA Function environment:
   - `SENDGRID_API_KEY` = your SendGrid key
   - `EMAIL_TO` = destination email (your inbox)
   - `EMAIL_FROM` = verified sender (configure in SendGrid)
4. **Set GitHub secret**:
   - `AZURE_STATIC_WEB_APPS_API_TOKEN` = deployment token from SWA.
5. **Push to main** – GitHub Actions will deploy automatically.

## Local development
- Install dependencies:
  ```bash
  cd api
  pip install -r requirements.txt
```