# 예외 정보

try:
    file = open('존재하지않는파일.txt')
    line = file.readline()
    print(line)
except OSError as err:
    print('예외 정보 : ', err.args)         # err.args : 예외 정보를 가진 변수
    print('예외 번호 : ', err.args[0])      # args[0] : 에러번호
    print('예외 메시지 : ', err.args[1])    # args[1] : 에러 메시지
    print('예외 정보 : ', err)              # err: __str__메소드에 의해 예외정보가 출력됨
except:
    print('알 수 없는 예외 발생...')
else:
    print('정상적으로 파일을 읽어왔습니다.')

