
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig , MessageType
from app.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME = settings.MAIL_USERNAME,
    MAIL_PASSWORD = settings.MAIL_PASSWORD,
    MAIL_FROM = "fake.hsr01@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME = settings.MAIL_FROM_NAME,
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

fastmail = FastMail(conf)


async def sendMail(recipients , subject , html):
    message = MessageSchema(
        subject=subject,
        body=html,
        recipients=recipients,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return True



