

import pandas as pd
# import sys

path = 'C:/Huey/GIT/Python01-1/Day09~/CSV/'
input_file = path + 'input/' + input('입력 파일 : ')
output_file = path + 'output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file, header=None)

print('삭제 전')
print(data_frame)

# drop()
# : 데이터프레임의 특정 행을 삭제하는 함수
data_frame = data_frame.drop([1,2,10,11,12])

print('삭제 후')
print(data_frame)

# iloc[0]
# : index 를 기준으로 특정 행, 열을 선택하는 함수
data_frame.columns = data_frame.iloc[0]

# reindex()
# : 데이터프레임에서 행을 재구성하는 함수

# data_frame.reindex(data_frame.index.drop(3))
# - 인덱스 3인 생을 삭제 후, 삭제된 새로운 데이터프레임을 재구성하여 반환
print('iloc[0] 이후')
print(data_frame)

# data_frame = data_frame.reindex(data_frame.index.drop(3))

new_index = range( len(data_frame) )
data_frame = data_frame.reindex( new_index )


data_frame.reset_index()
print('reset_index()')
print(data_frame)


print('reindex() : 인덱스 재구성 후')
print(data_frame)
data_frame.to_csv(output_file, index=True)