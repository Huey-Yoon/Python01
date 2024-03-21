# 자판기에 금액을 입력하고
# 커피의 잔 수에 따라서 남은 금액을 출력하세요.

# 한잔 : 300원
# 입력 금액 : 1400원
# (출력)
# 커피 1잔, 1100원
# 커피 2잔, 800원
# 커피 3잔, 500원
# 커피 4잔, 200원


a = input('투입 금액: ')
i = 1
a = int(a)

# while a >= 300:
while a // 300 > 0:
    print('커피 {}잔, {}원'.format(i, a-300))
    i += 1
    a -= 300
    
"""
    순서도
    1. 금액을 입력받는다.
    2. 잔돈을 계산한다.
        수식 : (금액) = (금액) - (커피금액)
    3. 커피 잔 수를 세어준다.
    4. 2~3번의 과정을 반복한다.
        *반복조건 : (금액) > 0
        
"""