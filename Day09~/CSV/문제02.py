'''

    문제 02.csv 파일을 입력받아
    전화번호 컬럼의 데이터에 대하여
    전화번호 형식의 정규표현식으로 매칭되는
    데이터만 추출하시오.

'''

import pandas as pd
import re

path = 'C:/Huey/GIT/Python01-1/Day09~/CSV/'
input_file = path + 'input/' + input('입력 파일 : ')
output_file = path + 'output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)

condition = r'^\d{2,3}-\d{3,4}-\d{4}$'
data_frame_match_pattern = data_frame.loc[data_frame['전화번호'].str.match(condition)]

data_frame_match_pattern.to_csv(output_file, index = False)