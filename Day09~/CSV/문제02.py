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


# match(정규표현식) : 문자열에서 정규표현식에 따라 패턴 매칭
# 전화번호 형식을 매칭하는 정규표현식
# : r'^\d{2,3}-\d{3,4}-\d{4}$'
condition = re.compile(r'^\d{2,3}-\d{3,4}-\d{4}$')
data_frame_match_pattern = data_frame.loc[data_frame['전화번호'].str.match(condition)]



# (추가문제 1) 전화번호 형식이 매칭되지 않는 행을 추출하시오.
# data_frame_match_pattern = data_frame.loc[~(data_frame['전화번호'].str.match(condition))]



# (추가문제 2) 전화번호 형식이 매칭되지 않는 행의, 전화번호 열만 추출하시오.
# ✅ 시리즈 개체의 부정연산(NOT) 시에는 ~ 기호를 사용한다.
# data_frame_match_pattern = data_frame.loc[~(data_frame['전화번호'].str.match(condition)), '전화번호']



data_frame_match_pattern.to_csv(output_file, index = False)

