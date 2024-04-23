# 서울시 지역별 미세먼지 농도
# 필요한 라이브러리
import os
import pandas as pd

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/day.xlsx'

# 엑셀파일 입력
dust_data = pd.read_excel(input_file)

# A, B 지역 데이터만 추출
dust_data_select = dust_data[["날짜", "금천구", "중랑구"]]
print(dust_data_select.head())  # 데이터프레임의 5개 행
print('-'*50)

# 결측치 확인
# : 값이 비어있는 부분
print("결측치")
print(dust_data_select.isna().sum())
print('-'*50)

# A, B 지역별 미세먼지 농도 기술통계량
print("금천구 미세먼지 기술통계량")
print(dust_data_select["금천구"].describe())
print('-'*50)

print("중랑구 미세먼지 기술통계량")
print(dust_data_select["중랑구"].describe())
print('-'*50)

# A, B 지역 미세먼지 농도 상자 그림 그래프
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

plt.figure(figsize=(8,6))   # 가로 8인치, 세로 6인치 크기
dust_data_select.boxplot(column = ["금천구", "중랑구"])
plt.title("미세먼지")
plt.xlabel("지역")
plt.ylabel("농도")

plt.show()