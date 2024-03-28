# 데코레이터
# : 다른 ㅎ마수를 받아 그 함수의 기능을 확장하거나 수정할 수 있는 함수

# 데코레이터 함수 정의
def my_decorator(func):
    # 내부 함수 정의
    def wrapper():
        print('함수가 호출되기 전...')
        func()      # 입력받은 함수 호출
        print('함수 호출 후...')
    return wrapper

# 데코레이터를 사용하여 sample() 함수에 장식
@my_decorator
def sample():
    print('데코레이터 함수로 장식된 함수...')

sample()


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()