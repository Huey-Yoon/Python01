
class Mul:

    def __init__(self, m):
        self.m = m

    def __call__(self, n):
        return self.m * n
    

mul3 = Mul(3)
mul5 = Mul(5)

print(mul3(10))
print(mul5(10))


# 커스텀으로 변형

m = int(input('m = '))
n = int(input('n = '))

print(Mul(m)(n))