from datetime import datetime
from fastapi import HTTPException
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from config.settings import settings, db


MAX_NOTIFICATIONS = 10


class EmailSender:
    def __init__(
        self,
        smtp_email,
        smtp_name,
        email,
        smtp_host,
        smtp_port,
        smtp_login,
        smtp_password,
    ):
        self.smtp_email = smtp_email
        self.smtp_name = smtp_name
        self.email = email
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_login = smtp_login
        self.smtp_password = smtp_password

    def send_email(self, subject, message, recipient=None):
        msg = MIMEText(message, "plain")
        msg["From"] = formataddr(
            (str(Header(self.smtp_name, "utf-8")), self.smtp_email)
        )
        msg["To"] = recipient if recipient else self.email
        msg["Subject"] = subject

        server = SMTP_SSL(self.smtp_host, self.smtp_port)
        server.login(self.smtp_login, self.smtp_password)
        server.send_message(msg)
        server.quit()


sender = EmailSender(
    settings.SMTP.smtp_email,
    settings.SMTP.smtp_name,
    settings.EMAIL.email,
    settings.SMTP.smtp_host,
    settings.SMTP.smtp_port,
    settings.SMTP.smtp_login,
    settings.SMTP.smtp_password,
)


class Notification:
    def __init__(self, database, max_notifications):
        self.db = database
        self.max_notifications = max_notifications

    async def create_note(self, user_id, key, target_id, data):
        if not user_id or not key:
            raise HTTPException(status_code=400, detail="Missing user_id or key")

        user_notifications = await self.db.notifications.find(
            {"user_id": user_id}
        ).to_list(length=MAX_NOTIFICATIONS)
        if len(user_notifications) >= MAX_NOTIFICATIONS:
            raise HTTPException(status_code=400, detail="Too many notifications")

        timestamp = int(datetime.timestamp(datetime.now()))
        user_document = {
            "user_id": user_id,
            "is_new": True,
            "key": key,
            "target_id": target_id,
            "data": data,
            "timestamp": timestamp,
        }

        inserted_notification = await self.db.notifications.insert_one(user_document)
        notification_id = str(inserted_notification.inserted_id)


create_notification = Notification(database=db, max_notifications=MAX_NOTIFICATIONS)
