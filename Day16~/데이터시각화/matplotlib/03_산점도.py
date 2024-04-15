import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터
np.random.seed(0)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# 추세선 계산
# slope         : 기울기
# intercept     : 절편
# r_value       : (피어슨)상관계수 - 두 변수 간의 선형 관계의 강도와 방향
# -> 두 변수의 공분산을 각각의 표준편차의 곲으로 나눈 값.
# p_value       : 유의성 검정  (회귀식이 통계적으로 유의미한지)
# std_err       : 기울기 추정값의 표준오차
slope, intercept, r_value, p_value, std_err = linregress(x,y)
# 선 그래프 데이터
line = slope * x + intercept
plt.plot(x, line, color = 'orange', label='추세선')

print('절편 : {}'.format(intercept))
print('p value : {}'.format(p_value))

# 그래프 설정
# s: 점의 크기
plt.scatter(x, y, edgecolors= 'black', color = 'blue', s=10)

# 제목 및 라벨
plt.title('산점도 데이터')
plt.xlabel('X축')
plt.ylabel('Y축')

# 그래프 이미지 저장
plt.savefig('산점도.png', dpi=400)

# 그래프 출력
plt.show()