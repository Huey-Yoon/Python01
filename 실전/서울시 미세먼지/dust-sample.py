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

# 지역별 미세먼지 농도 등분상성 검정 및 평균 차이 검정
from scipy.stats import bartlett, levene, f_oneway

# 등분산성 ?
# : 실제 관측값과 예측한 값 사이의 차이(잔차)로 구한 분산이
#   값의 영향을 미치는 변수에 따라서 일정한 성질을 가지는 것

print("금천구-중랑구 등분산성을 검정")

# bartlett 를 사용하여 분산의 등분산성을 검정 / 표본이 정규성을 만족할 때만 사용 가능
A = dust_data_select["금천구"]
B = dust_data_select["중랑구"]

# 결측치 (NaN) 제거
A = A.dropna()
B = B.dropna()
# A[~pd.isna()]

bartlett_statistic, bartlett_p_value = bartlett(A, B)

# 통계량: 7.09 / p-value: 0.0077 < 0.05 (유의미한 수준으로 등분산성이 깨짐)
print('bartlett 검정 - 통계량 : ', bartlett_statistic, 'p-value : ', bartlett_p_value)
print('-'*50)

# levene 등분산성 검정
levene_statistic, levene_p_value = levene(A, B)

# 통계량: 0.5013 / p-value: 0.4817 > 0.05 (유의미한 수준으로 등분산성 전제)
print('levene 검정 - 통계량 : ', levene_statistic, 'p-value : ', levene_p_value)
print('-'*50)


# 지역 평균 차이 검정
from scipy.stats import ttest_ind

# equal_var = 등분산성 만족 여부
t_statistic, p_value = ttest_ind(A, B, equal_var=True)
print("t_statistic : ", t_statistic)
print("p_value : ", p_value)
print('-'*50)
# p_value: 0.3199 > 0.05

print('##### 결론 도출 #####')
if p_value > 0.05:
    print("귀무가설 채택 - 서울 금천구와 중랑구는 미세먼지 농도의 평균에 차이가 없다.")
else:
    print("대립가설 채택 - 서울 금천구와 중랑구는 미세먼지 농도의 평균에 차이가 있다.")




# A, B 지역 미세먼지 농도 상자 그림 그래프
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

plt.figure(figsize=(8,6))   # 가로 8인치, 세로 6인치 크기
dust_data_select.boxplot(column = ["금천구", "중랑구"])
plt.title("미세먼지")
plt.xlabel("지역")
plt.ylabel("농도")

plt.savefig(path + '/미세먼지 농도 비교.png')
plt.show()

