

import pandas as pd
# import sys

path = 'C:/Huey/GIT/Python01-1/Day09~/CSV/'
input_file = path + 'input/' + input('입력 파일 : ')
output_file = path + 'output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)

# 선택할 열 리스트
# loc[ 행라벨, 열라벨 ]
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]

data_frame_column_by_name.to_csv(output_file, index=False)

