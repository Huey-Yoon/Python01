
# 이터레이터

list = [1,2,3,4,5]

# 방법 1
iter_obj = iter(list)
for i in list:
    print( i )

# 방법 2
iter_obj = iter(list)
i1 = 0
while i1 < len(list):
    print( next(iter_obj) )
    i1 += 1

# 방법 3
iter_obj = iter(list)
while True:
    next_element = next(iter_obj, None) # 다음요소가 없으면 None
    if next_element is None:
        print('마지막')
        break
    print(next_element)


# 응용
iter_obj = iter(list)
while True:
    next_element = next(iter_obj, None)
    if next_element is None:
        break

    print(next_element, end="")
    if next_element is not None:
        print(',', end='')
