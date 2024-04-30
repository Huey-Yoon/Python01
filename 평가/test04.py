# 아래의 [보기]의 막대 그래프를 출력하기 위한 코드를 완성하시오.

# 보기
# 주어진 코드
# 국내 휴양림 분포
# pip install xlrd==2.0.1
import os
import pandas as pd
import matplotlib.pyplot as plt
# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/forest.xls'

# 엑셀 파일 입력
forest_data = pd.read_excel(input_file)

# 변수명 변경
forest_data.columns = ["name", "city", "gubun", "area", "number","code","codename","new_city"]

# 시도별 휴양림 빈도분석
# - value_counts() 함수
city_counts = forest_data['city'].value_counts()

# 막대 그래프로 데이터 시각화
city_counts.plot(kind='bar', title='city')
plt.show()

plt.show()