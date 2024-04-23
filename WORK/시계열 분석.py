
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# 엑셀 파일에서 데이터 불러오기
data = pd.read_excel('C:/Users/user/Desktop/Huey/Python01/WORK/loss.xlsx')

# Prophet 모델 초기화
model = Prophet()

# 날짜와 손해율 칼럼을 가지고 예측 모델 학습
data.columns = ['ds','y']       # 날짜 칼럼 이름을 'ds', 손해율 칼럼 이름을 'y'로 변경
model.fit(data)

# 미래 데이터프레임 생성
future = model.make_future_dataframe(periods=30)    # 예측할 기간은 30일로 설정

# 미래에 대한 예측 수행
forecast = model.predict(future)

# 예측 결과 확인
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# 결과 시각화
model.plot(forecast)
plt.xlabel('Data')
plt.ylabel('Loss Ratio')
plt.title('Loss Ratio Forecast')
plt.show()

