import smtplib
from email.mime.text import MIMEText
import csv

smtp_info = {
    "smtp_server": "smtp.naver.com",
    "smtp_user_id": "09pc@naver.com",
    "smtp_user_pw": "dbswjdgus13245",
    "smtp_port": 587
}

def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        server.starttls()
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        server.sendmail(msg['From'], msg['To'], msg.as_string())

def read_csv():
    path = 'C:/Huey/GIT/Python01-1/Day08/'
    file_path = path + 'custom.csv'

    with open(file_path, 'r', newline='', encoding='UTF-8') as file:
        csv_reader = csv.reader(file, delimiter=',', quotechar="'")
        return list(csv_reader)

custom_csv = read_csv()

for line in custom_csv:
    receiver = line[1]
    sender = smtp_info['smtp_user_id']
    title = line[2]
    content = line[3]

    msg = MIMEText(content, _charset="utf-8")
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = receiver

    send_email(smtp_info, msg)
