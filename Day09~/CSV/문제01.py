
"""

    supplier_data.csv 파일을 입력하여
    Supplier Y 공급업체 또는 Supplier Z 공급업체라면, 가격이 650 초과인
    데이터를 문제01.csv 파일로 출력하시오.

"""

import pandas as pd

path = 'C:/Huey/GIT/Python01-1/Day09~/CSV/'
input_file = path + 'input/' + input('입력 파일 : ')
output_file = path + 'output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)

# Supplier Y, Supplier Z 공급업체 집합으로 설정
supplier_company = [ 'Supplier Y', 'Supplier Z' ]

# 가격에 $ 표시 삭제, 실수로 표현
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

# 공급업체 집합 안에 있고, Cost가 650 초과인 건들만 출력
data_frame_list = data_frame.loc[(data_frame['Supplier Name'].isin(supplier_company)) & (data_frame['Cost'] > 650.0), : ]

data_frame_list.to_csv(output_file, index = False)


# Supplier Y 공급업체, 또는 Supplier Z 공급업체라면 가격이 650 초과인 데이터 필터 조건.
# condition = (data_frame['Supplier Name'].str.contains('Y')) | (data_frame['Supplier Name'].str.contains('Z') & (data_frame['Cost'] > 650.0))

