# 

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration     # raise : 이터레이터 끝 강제 발생
        result = self.data[self.position]
        self.position += 1
        return result
    

my = MyIterator([1,2,3,4,5])
for i in my:
    print(i)



# iter_obj = iter(my)
# print(next(iter_obj))
# print(next(iter_obj))

