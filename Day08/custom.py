
# csv 리스트에 있는 사람들에게 보내기

import smtplib
from email.mime.text import MIMEText # 이메일 텍스트 형식 모듈

print('네이버 이메일 보내기')
print('로그인')


smtp_info = dict({"smtp_server" : "smtp.naver.com",         # SMTP 서버 주소
                  "smtp_user_id" : "09pc@naver.com",
                  "smtp_user_pw" : "dbswjdgus13245",
                  "smtp_port" : 587})                       # SMTP 서버 포트

def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS 보안 연결
        server.starttls()
        # 로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        
        
        # 로그인 된 서버에 이메일 전송
        response = server.sendmail(msg['from'], msg['to'], msg.as_string()) # 메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.
        
        # 이메일을 성공적으로 보내면 결과는 {}
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print('응답결과: ')
            print(response)

import csv        
def read_csv():
    path = 'C:/Huey/GIT/Python01-1/Day08/'
    file = path + 'custom.csv'

    with open(file, 'r', newline='', encoding='UTF-8') as file:
    # reader(파일객체, delimiter(구분기호), quotechar(문자열기호))
    # quotechar : 나뉘면 안되는 데이터를 어떤 기호로 묶을지 지정
        csv_reader = csv.reader(file, delimiter=',', quotechar="'")

        return list(csv_reader)

# 이메일 내용

custom_csv = read_csv()

# csv 파일 전체 인원에 메일 발송
for line in custom_csv:
    receiver = line[1]                      # 받는 사람
    sender = smtp_info['smtp_user_id']      # 보내는 사람
    title = line[2]
    content = line[3]

    # 메일 객체 생성
    msg = MIMEText(_text = content, _charset = "utf-8")
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = receiver

    # 이메일 전송
    send_email(smtp_info, msg)
    