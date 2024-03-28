# 데코레이터 함수

import time

def elapsed(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print('함수 수행 시간 : {} 초'.format(end-start))
        return result
    return wrapper

@elapsed
def my_fuc():
    time.sleep(3)       # 3초간 프로그램 지연
    print('함수 수행')

my_fuc()
