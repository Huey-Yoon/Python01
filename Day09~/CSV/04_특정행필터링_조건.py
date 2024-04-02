

import csv
# import sys

path = 'C:/Huey/GIT/Python01-1/Day09~/CSV/'
input_file = path + 'input/' + input('입력 파일 : ')
output_file = path + 'output/' + input('출력 파일 : ')

with open(input_file, 'r', newline='', encoding='utf-8') as csv_in_file:
	with open(output_file, 'w', newline='', encoding = 'utf-8') as csv_out_file:
		filereader = csv.reader(csv_in_file)            # csv 읽기 모드 객체 생성
		filewriter = csv.writer(csv_out_file)           # csv 쓰기 모드 객체 생성
		header = next(filereader)                       # 첫 행을 입력
		filewriter.writerow(header)                     # 첫 행을 출력
		for row_list in filereader:
			supplier = str(row_list[0]).strip()                     # 공급업체명
			cost = str(row_list[3]).strip('$').replace(',', '')     # 가격
			# 조건으로 특정행 필터
			if supplier == 'Supplier Z' and float(cost) > 600.0:
				filewriter.writerow(row_list)
				
