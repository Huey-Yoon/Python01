
# 많은 모듈을 포함할 때, 모듈을 구분하기 좋다.
# import secure as S

# 적은 모듈을 퐇마할 때, 쉽게 쓸 수 있다.
from secure import *

# 사용자 정보 마스킹하기

name = '윤정현'
no = '961208-1234567'
phone = '010-4511-9615'

print(name)
print(no)
print(phone)
print()

print( secure_name(name) )
print( secure_no(no) )
print( secure_phone(phone) )
