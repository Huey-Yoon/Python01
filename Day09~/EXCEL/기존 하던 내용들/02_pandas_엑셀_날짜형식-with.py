

#!/usr/bin/env python3
import pandas as pd
# import sys

path = 'C:/Huey/GIT/Python01-1/Day09~/EXCEL/'
input_file = path + 'input/' + input('입력 파일 : ')
output_file = path + 'output/' + input('출력 파일 : ')

# read_excel( ) : 엑셀 파일 읽어들여서, 데이터프레임으로 반환
data_frame = pd.read_excel(input_file, sheet_name='january_2013')

# to_excel( 출력객체, sheet_name='시트이름', index=여부)
# : 데이터 프레임을 엑셀 파일로 변환하여 저장하는 함수

# ExcelWriter() 함수로 출력 객체 생성 시에는
# 반드시 출력 후 close() 를 해야한다.  (with 구문을 쓰면 close() 자동으로 된다.)
with pd.ExcelWriter(output_file) as writer:
    # to_excel() 함수를 사용하여 데이터프레임을 엑셀 파일로 변환하여 저장
    data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)

# 파일 출력 후, 메모리 해제 close() 함수를 호출해주어야한다.
print("Excel 파일이 성공적으로 생성되었습니다.")
