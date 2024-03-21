# 모듈
'''
    모듈이란?
    : 변수나 함수 또는 클래스를 모아놓은 파이썬 파일
    - 하나의 파이썬 파일(.py)
    
    모듈 사용
    : import 모듈명
'''

import converter as C
# import (모듈) 사용할 때는 함수 앞에 (모듈).함수

from converter import *

# 150km --> miles 단위로 변환
miles = C.kilometer_to_miles(150)
print('150km {} miles'.format( miles ))

# 1000g --> pound 로 변환
pound = C.gram_to_pound(1000)
print('1000g = {} pound'.format( pound ))

