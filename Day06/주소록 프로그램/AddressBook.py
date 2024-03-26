'''
    주소록 프로그램 만들기
    윤정현, 010-4511-9615, 인천시 부평구

    [기능]
    1. 새로운 주소 등록하기
    2. 기존 주소 삭제하기
    3. 기존 주소 수정하기
    4. 특정 주소 검색하기
    5. 전체 주소 출력하기
    6. 주소록 정보를 파일로 관리하기

    [객체]
     AddressBook - 주소록 객체
     Person      - 사람 객체

    [주소록 정보]
    - AddressBook.csv 파일로 관리
    - 이름, 전화번호, 주소 정보를 저장

    [주소록 함수]
    file_reader()           : AddressBook.csv 파일 읽기
    file_generator()        : AddressBook.csv 파일 생성
    menu()                  : 메뉴 소개 및 입력
    exit()                  : 프로그램 종료
    run()                   : 프로그램 실행
    insert()                : 추가
    update()                : 수정
    search()                : 검색
    print_all()                : 전체 출력
    
    __init__()              : 생성자 - 주소록 리스트, 파일객체 초기화
'''

# 사람 : Person 클래스
# ✅ 생성자
#   - 변수 : name, phone, addr 
# ✅ info() 
#   - 이름, 전화번호, 주소를 문자열 템플릿으로 출력하는 기능


# 주소록 : AddressBook 클래스
# ✅ 변수 : 주소록 리스트 - address_list
# ✅ 생성자
# ✅ 메소드
#    file_reader()           : AddressBook.csv 파일 읽기
#    file_generator()        : AddressBook.csv 파일 생성
#    menu()                  : 메뉴 소개 및 입력
#    exit()                  : 프로그램 종료
#    run()                   : 프로그램 실행
#    insert()                : 추가
#    update()                : 수정
#    search()                : 검색
#    print_all()             : 전체 출력
# ------------------------------------------------------
import sys

# 사람
class Person:
    # 생성자
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    # info()
    def info(self):
        print('{}, {}, {}'.format(self.name, self.phone, self.addr))


# 주소록
class AddressBook:
   # 생성자
   def __init__(self):
       self.address_list = []

   # csv 파일 읽기
   def file_reader(self):
       pass
   
   # csv 파일 생성
   def file_generator(self):
       try:
           file = open('AddressBook.csv','wt', encoding='UFT-8')
       except:
           print('AddressBook.csv 파일을 생성할 수 없습니다.')
       else:
           # address_list 를 모두 반복하여, 모든 연락처를 csv 파일에 출력
           for person in self.address_list:
               file.write('{},{},{}\n'.format(person.name, person.phone, person.addr))
               file.close()
   
   # 메뉴
   def menu():
       print('-' * 30)
       print('1. 주소 등록하기')
       print('2. 주소 삭제하기')
       print('3. 주소 수정하기')
       print('4. 주소 검색하기')
       print('5. 모든 주소 출력하기')
       print('0. 프로그램 종료')
       choice = int( input('메뉴번호 : '))
       return choice
   
   # 프로그램 종료
   def exit(self):
       print('프로그램을 종료합니다.')
       sys.exit()           # 자동 임포트 : ctrl + . (quick fix)
   
   # 프로그램 실행
   def run(self):
       while True:
            choice = AddressBook.menu()
            if choice == 0: self.exit()         # 종료
            elif choice == 1: self.insert()     # 추가
            elif choice == 2: self.delete()     # 삭제
            elif choice == 3: self.update()     # 수정
            elif choice == 4: self.search()     # 검색
            elif choice == 5: self.print_all()  # 전체출력
            else: print('(0~5) 사이의 메뉴번호를 입력해주세요.')
   
   # 주소록 추가
   def insert(self):
       print('---- 연락처 추가 ----')
       name = input('이름 : ')
       phone = input('전화번호 : ')
       addr = input('주소 : ')
       
       # 유효성 검사
       if name or phone or addr:
        person = Person(name, phone, addr)
        self.address_list.append(person)
       # csv 파일에 연락처 목록을 생성(overwrite)
        self.file_generator()
        print('새 연락처가 등록되었습니다!')
       else:
           print('누락된 입력값이 있어 등록되지 않았습니다.')
   
   # 주소록 삭제
   def delete(self):
       pass
   
   # 주소록 수정
   def update(self):
       pass
   
   # 주소록 조회
   def search(self):
       pass
   
   # 전체 출력
   def print_all(self):
       pass


# AddressBook 클래스 끝

# 객체 생성
my_app = AddressBook()

# 프로그램 실행 - run()
my_app.run()

