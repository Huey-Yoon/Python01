# 리스트 내포
# : 리스트 내부에 for 문을 사용하여
#   리스트 요소를 효율적으로 저장하는 방식

# 문법
#           리스트 = [표현식 for 변수 in 컬렉션]

# [1,2,3,4,5]  -->  [2,4,6,8,10]


li1 = [1,2,3,4,5]

# 리스트 내포 사용 X
newList = []
for i in li1:
    newList.append(i*2)
print('newList : ',newList)

# 리스트 내포 사용 O
li = [ 2 * n for n in li1]
print('li : ',li)

a = [ 10 * n for n in li1 if n%2==0]
print('a : ',a)

b = [ 10 * n for n in li1 if n%2==1]
print('b : ',b)
