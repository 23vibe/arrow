import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

class EmailProvider:
    def __init__(self):
        api_key = os.environ.get("BREVO_API_KEY")
        if not api_key:
            raise RuntimeError("BREVO_API_KEY not configured")
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key["api-key"] = api_key
        #add more brevo sdk config settings
        self.api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    def send(self, subject: str, content: str, to_email: str, from_email: str):
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": to_email}],
            sender={"email": from_email},
            #add more settings (response to)
            subject=subject,
            html_content=content
        )
        try:
            response = self.api_instance.send_transac_email(send_smtp_email)
            return response
        except ApiException as e:
            print(f"Failed to send email: {e}")
            raise
