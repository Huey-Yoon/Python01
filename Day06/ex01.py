# open(파일명, 모드, 옵션) : 파일을 열 때 사용되는 함수, 파일 경로와 옵션을 인자로 받습니다.
# read() : 파일에서 데이터를 읽어옵니다.
# write() : 파일에 데이터를 씁니다.
# close() : 파일을 닫습니다.
# readline() : 파일에서 한 줄씩 데이터를 읽어옵니다.
# readlines() : 파일에서 모든 줄을 읽어와 리스트로 반환합니다.


# 텍스트 파일 생성

# 파일 저장 경로
path = 'C:/Huey/GIT/Python01-1/Day06/file/'
file = open(path + 'hello.txt', 'wt', encoding = 'UTF-8')


# 파일 내에서 출력 : write()
file.write('안녕하세요')
file.write('\n')
file.write('윤정현입니다.')
# file.write('새로운 내용을 추가합니다.')
print('파일이 생성되었습니다.')

# 파일 닫기
file.close()
