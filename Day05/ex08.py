# try:
    # 예외 발생 가능한 코드
    # 예외가 발생하면 여기에서 처리됨
# except 예외종류 as 변수:
    # 예외 처리 코드
# finally:
    # 항상 실행되는 코드 (선택사항)



# 예외를 따로 처리하는 방법
print('X / Y')

try:
    X = int( input('X : ') )
    Y = int( input('Y : ') )
    result = X / Y
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')
except ValueError:
    print('숫자만 입력 가능합니다')
except:
    print('알 수 없는 예외가 발생하였습니다')
else:
    print(result)
