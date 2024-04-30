# 아래의 [보기]의 주어진 코드를 활용하여, 다음 요구사항에 프로그램을 완성하시오.

# 보기
import pandas as pd
import os

# 현재 실행 파일 경로 가져오고, 입력파일 지정하기
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

# 형식으로 변환
# TODO: 아래와 같이 날짜 형식을 지정하여 출력되도록 코드를 작성하시오.
#   Purchase Date 열의 데이터의 날짜형식을 지정한다.
#   yyyy-mm-dd ---> yyyy/mm/dd
dates = data_frame['Purchase Date']
dates = pd.to_datetime(dates).dt.strftime('%Y/%m/%d')
data_frame['Purchase Date'] = dates


writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='out_january_2013', index=False)
writer.close()

