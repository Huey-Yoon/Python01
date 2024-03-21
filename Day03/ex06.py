# 중첩 반복문
# : 반복문 안에 또 하나의 반복문을 작성

# 구구단 전체 출력
# i = 2~9단
# j = 1~9까지 곱해진다.

for i in range(2,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))
    print()


for i in range(2,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))
    print()