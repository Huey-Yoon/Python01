
class Person:
    # 생성자
    def __init__(self, name, age=0, tel=None):
        self.name = name
        self.age = age
        self.tel = tel
    
    # 메소드
    def show_info(self):
        print('이름 : {}, 나이 : {}, 전화번호 : {}'.format(self.name, self.age, self.tel))
        

# Person 객체 생성
person = Person('김조은', 20, '010-1234-1234')
person.show_info()

person2 = Person('김조은', 20, '010-1234-1234')
person2.show_info()

# 객체의 변수 접근
print('이름 : {}'.format(person.name))
print('나이 : {}'.format(person.age))
print('전화번호 : {}'.format(person.tel))
        
        
# 생성자를 디폴트 매개변수로 지정하면,
# 인자의 개수를 가변적으로 사용가능
person3 = Person('이조은')
person3.show_info()

person4 = Person('권조은', 10)
person4.show_info()

person4.tel = '010-2222-3333'
print('person4 추가된 전화번호 : {}'.format(person4.tel))