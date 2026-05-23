import resend

from app.config import settings


resend.api_key = settings.RESEND_API_KEY


async def send_verify_email(
    email: str,
    verify_url: str
):

    params = {
        "from": "onboarding@resend.dev",
        "to": [email],
        "subject": "Verifique seu email",
        "html": f"""
            <h1>Confirmar Email</h1>

            <a href="{verify_url}">
                Clique aqui para verificar
            </a>
        """
    }

    resend.Emails.send(params)