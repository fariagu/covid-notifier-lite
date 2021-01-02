import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(covid_report: dict):
    smtp_server = os.environ.get('SMPT_SERVER')
    port = os.environ.get('SMTP_PORT')
    email = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('EMAIL_PASSWORD')
    receiver = os.environ.get('RECEIVERS')
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(email, password)

        msg = MIMEMultipart()
        msg["From"] = "Covid Report Notifier"
        msg["To"] = receiver
        msg["Subject"] = f"""Covid Report - {covid_report["report_no"]}"""

        message = f"""
        <p>{covid_report["download_url"]}</p>
        """

        msg.attach(MIMEText(message, "html"))

        server.send_message(msg)

        server.quit()
