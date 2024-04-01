
# 정규 표현식
# 이메일 형식 체크

import re

def check_email(email):
    pattern = r'^[a-zA-Z0-9+._-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # 분석
    # 1 : [a-zA-Z0-9+._-]   : A
    #        a-zA-Z0-9      : 영문자 또는 숫자로 1개 이상
    #        +._-           : 특수문자 ( + . _ - ) (단, 첫글자는 불가)
    # 2 : [a-zA-Z0-9+._-]+  : A 패턴이 1글자 이상
    # 3 : @                 : @
    # 4 : [a-zA-Z0-9-]+     : 영문자 또는 숫자 또는 특수문자 ( - )로 1글자 이상
    # 5 : \.                : 1글자 대체가 아닌 문자 . 을 의미
    # 6 : [a-zA-Z0-9-.]     : 영문자 또는 숫자 또는 특수문자 ( - . )로 1글자 이상
    if re.match(pattern, email):
        return True
    else:
        return False

# 테스트
email = input("이메일 : ")
if check_email(email):
    print("유효한 이메일 주소입니다.")
else:
    print("유효하지 않은 이메일 주소입니다.")
