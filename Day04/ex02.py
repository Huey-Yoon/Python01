# 시퀀스 내장 함수

# enumerate()
'''
    (0, 'C언어')
    (1, '파이썬')
    (2, 'JAVA')
'''

prog = ['C언어', '파이썬', 'JAVA']
for item in enumerate(prog):
    print(item)

# range()
for i in range(2,21,2):
    print(i, end=' ')
print()

# len()
li = ['월','화','수','목','금','토','일']
print(li)
print('li의 요소의 개수 : {}'.format( len(li) ))

# sorted
# - 해당 리스트를 정렬한 새 리스트를 반환하는 함수
# * sorted( 리스트, reverse=False ) : 오름차순
# * sorted( 리스트, reverse=True) : 내림차순

scores = [100,90,65,80,70]
print( sorted(scores) )         # 기본이 오름차순임.
print( sorted(scores, reverse=False) )
print( sorted(scores, reverse=True) )

# zip
names = ['아이유', '최민식', '뉴진스', '원더걸스', '소녀시대']
for student in zip(names, scores):
    print(student)