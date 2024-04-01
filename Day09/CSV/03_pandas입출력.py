


# import sys
import pandas as pd

path = 'C:/Huey/GIT/Python01-1/Day09/CSV/'
input_file = path + 'input/' + input('입력 파일 : ')
output_file = path + 'output/' + input('출력 파일 : ')

# 데이터 프레임
data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)         # index = False : csv파일에 index 열 제외
# data_frame.to_csv(output_file, index=True)        # index = True  : csv파일에 index 열 출력
