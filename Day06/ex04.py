
# 파일 삭제

import os

path = 'C:/Huey/GIT/Python01-1/Day06/file/'
file = input('삭제할 파일명 : ')
file = path + file

# 파일 존재 여부확인
if os.path.exists(file):

    # 파일 삭제
    os.remove(file)
    print('파일이 삭제되었습니다.')
else:
    print('파일을 찾을 수 없습니다.')