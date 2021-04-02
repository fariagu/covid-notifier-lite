import os
import telegram_send

api_id = os.environ.get('TELEGRAM_API_ID')
api_hash = os.environ.get('TELEGRAM_API_HASH')
phone_nr = os.environ.get('TELEGRAM_PHONE_NR')

# telegram_send.send(messages=["Notificaton!!!"])

def send_telegram(covid_report: dict):
    messages = [
        f"""Covid Report - {covid_report["report_no"]}""",
        covid_report["download_url"]
    ]

    telegram_send.send(messages=messages)
