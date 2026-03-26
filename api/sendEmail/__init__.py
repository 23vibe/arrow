import json
import logging
import os
import re
import azure.functions as func
from .email_provider import EmailProvider

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    #get form info
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()
    # print(name, email, message)
    
    if not name or not email or not message:
        return func.HttpResponse("Missing fields", status_code=400)
    if not EMAIL_RE.match(email):
        return func.HttpResponse("Invalid email", status_code=400)

    try:
        provider = EmailProvider()
        to_email = "veronika.majickova@gmail.com" #os.environ.get("EMAIL_TO")
        from_email = os.environ.get("EMAIL_FROM")
        if not to_email or not from_email:
            return func.HttpResponse("Email settings not configured", status_code=500)

        subject = f"New contact from {name}"
        content = f"From: {name}: {email} \n\n{message}"
        provider.send(subject, content, to_email=to_email, from_email=from_email)

        return func.HttpResponse(json.dumps({"status": "ok"}), status_code=200, mimetype="application/json")
    except Exception as e:
        logging.exception("Failed to send email")
        return func.HttpResponse("Failed to send email", status_code=500)
