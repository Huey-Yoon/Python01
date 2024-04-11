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
    print_all()             : 전체 출력
    
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
import pymysql

# MySQL 서버에 접속
conn = pymysql.connect(
    host='127.0.0.1',
    user='joeun',
    password='123456',
    database='joeun',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 사람
class Person:
    # 생성자
    def __init__(self, no, name, tel, address):
        self.no = no
        self.name = name
        self.tel = tel
        self.address = address
        
    # info()
    def info(self):
        print('{}, {}, {}, {}'.format(self.no, self.name, self.tel, self.address))

# 주소록
class AddressBook:

    # 생성자
    def __init__(self):
        self.address_list = []
        # self.file_reader()

    # csv 파일 읽기
    def file_reader(self):
        try:
            # 예외 발생 가능성 코드
            file = open('AddressBook.csv', 'rt', encoding='UTF-8')
        except:
            # 예외 처리 
            print('AddressBook.csv 파일이 없습니다.')
        else:
            # 예외 미발생 시, 파일 입력(AddressBook.csv --> address_list)
            while True:
                buffer = file.readline()    # 한 줄씩 데이터 읽기
                if not buffer:
                    break
                # 김조은,010-1234-1234,인천시 부평구(\n)
                name = buffer.split(',')[0]
                phone = buffer.split(',')[1]
                addr = buffer.split(',')[2].rstrip('\n')
                # rstrip(문자) : 지정한 문자를 문자열 오른쪽에서 제거
                # Person 객체 생성
                person = Person(name, phone, addr)
                # 가져온 연락처 정보를 address_list 에 추가
                self.address_list.append(person)

            print('AddressBook.csv 파일을 읽어왔습니다.')
            file.close()

    # csv 파일 생성
    def file_generator(self):
        try:
            file = open('AddressBook.csv', 'wt', encoding='UTF-8')
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
        print('-' * 30)
        choice = int( input('메뉴 번호 : '))
        return choice

    # 프로그램 종료
    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()      # 자동 임포트 : ctrl + . (quick fix) 


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
        print('----- 연락처 추가 -----')
        name = input('이름 : ')
        phone = input('전화번호 : ')
        addr = input('주소 : ')
        
        result = 0
        # 유효성 검사
        if name and phone and addr:
            person = Person(0, name, phone, addr)
            result = self.insert_data(person)
        else:
            print('누락된 입력값이 있어 등록되지 않았습니다.')

        if result > 0:
            print('새 연락처를 등록하였습니다.')
        else:
            print('연락처가 등록되지 않았습니다.')

    # 주소록 삭제 
    def delete(self):
        print('----- 기존 연락처 삭제 -----')
        no = input('삭제할 번호 : ')
        if not no:
            print('번호가 입력되지 않아 삭제를 취소합니다.')
            return
        # 삭제 여부
        deleted = False

        no = int(no)

        name = ''
        person = self.select_data(no)

        if person == None:
            print('입력한 번호에 해당하는 연락처가 존재하지 않습니다.')
            return

        # 입력한 번호가 연락처에 존재하면,
        print('검색한 전화번호 : {}'.format(person.tel))
        if input('삭제할까요? (Y/N)').upper() == 'N' :
            return

        result = self.delete_data(no)

        if result > 0:
            print('{} 의 정보를 삭제하였습니다.'.format(name))
        else:
            print('{}의 정보가 삭제되지 않았습니다.'.format(name))

                    

    # 주소록 수정
    def update(self):
        # 1. 수정할 이름 입력
        print('----- 기존 연락처 수정 -----')
        no = input('수정할 기존 번호 검색 : ')

        # 2. 입력여부 체크
        if not no:
            print('번호가 입력되지 않아 수정을 취소합니다.')
            return
        
        # 3. 수정 여부 확인 (Y/N)
        updated = False
        
        no = int(no)

        name =''
        person = self.update_data(no)

        if person == None:
            print('입력한 번호에 해당하는 연락처가 존재하지 않습니다.')
            return
        print('검색한 전화번호 : {}'.format(person.tel))
        if input('수정할까요? (Y/N)').upper() == 'N' :
            return
        
        result = self.update_data(no)

        if result > 0:
        # 4. 수정할 이름/전화번호/주소 입력            
            new_name = input('수정할 이름 : ')
            new_tel = input('수정할 전화번호 : ')
            new_address = input('수정할 주소 : ')

            if new_name: self.address_list.name = new_name
            if new_tel: self.address_list.phone = new_tel
            if new_address: self.address_list.addr = new_address

            print('{} 의 정보를 수정하였습니다.'.format(name))
            return
        else:
            print('{}의 정보가 수정되지 않았습니다.'.format(name))

        # 5. 수정할 list의 요소에 갱신 - address_list[i].name = new_name
            updated = True
            print('주소록이 수정되었습니다!')
            print('수정된 주소록 정보')



    # 주소록 조회 
    def search(self):
        # 리스트에서 검색할 연락처 정보를 이름으로 찾아서 출력
        no = input('검색할 번호 : ')
        if not no: 
            print('번호가 입력되지 않아서 조회할 수 없습니다.')
            return      # 메소드 종료
        
        print('----- 조회된 연락처 정보 -----')
        
        # 데이터 조회 요청
        person = self.select_data(no)

        if person == None:
            print('조회된 연락처 없습니다.')
        else:
            person.info()


    # 전체 출력 
    def print_all(self):
        print('----- 전체 연락처 출력 -----')

        # 데이터베이스 조회 요청
        # 1. SELECT * FROM address_book 쿼리 요청
        # 2. 조회 결과를 address_list 에 저장

        address_list = self.select_list()

        for person in address_list:
            person.info()

        list_count = len(address_list)
        print('총 {}개의 연락처가 있습니다.'.format(list_count))





    # 데이터 목록 조회
    def select_list(self):
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM address_book"
                cursor.execute(sql)

                list = cursor.fetchall()
                address_list = []
                for person in list:
                    no = person.get('no')
                    name = person.get('name')
                    tel = person.get('tel')
                    address = person.get('address')
                    address_list.append(Person(no, name, tel, address))
                return address_list

        except pymysql.MySQLError as e:
            print('MySQL 에러 : ', e)
    # 데이터 목록 조회 끝

    # 데이터 등록
    def insert_data(self, person):
        try:
            result= 0
            # 커서 생성
            with conn.cursor() as cursor:
                # 데이터 등록
                sql = " INSERT INTO address_book (name, tel, address) "\
                    + " VALUES (%s,%s,%s) "

                # result = cursor.execute(sql)          # 쿼리 실행 요청
                data = (person.name, person.tel, person.address)
                result = cursor.execute(sql, data)
                print('{}행의 데이터 등록 완료'.format(result))
                
            # 변경사항 적용
            conn.commit()
            return result
            
        except pymysql.MySQLError as e:
            print("데이터 등록 중 에러 발생 : ", e)
    # 데이터 등록 끝

    # 데이터 삭제
    def delete_data(self, no):
        try:
            result = 0
            # 커서 생성
            with conn.cursor() as cursor:
                # 데이터 등록
                sql = " DELETE FROM address_book  "\
                    + " WHERE no = %s "

                # result = cursor.execute(sql)          # 쿼리 실행 요청
                result = cursor.execute(sql, no)
                print('{}행의 데이터 삭제 완료'.format(result))
                
            # 변경사항 적용
            conn.commit()
            return result
        except pymysql.MySQLError as e:
            print("데이터 삭제 중 에러 발생 : ", e)
    # 데이터 삭제 끝

    # 데이터 조회
    def select_data(self, no):
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM address_book"\
                    + " WHERE no = %s"
                cursor.execute(sql, no)

                person = cursor.fetchone()

                if person:
                    no = person.get('no')
                    name = person.get('name')
                    tel = person.get('tel')
                    address = person.get('address')
                    return Person(no, name, tel, address)
                else:
                    return None
                
        except pymysql.MySQLError as e:
            print('MySQL 에러 : ', e)
    # 데이터 조회 끝

    # 데이터 수정
    def update_data(self, no):
        try:
            result = 0
            # 커서 생성
            with conn.cursor() as cursor:
                # 데이터 등록
                sql = " UPDATE address_book  "\
                    + "     SET name = %s "\
                    + "     , tel = %s "\
                    + "     , address = %s "\
                    + " WHERE no = %s "

                # result = cursor.execute(sql)          # 쿼리 실행 요청
                cursor.execute(sql, new_name, new_tel, new_address, no)
                print('{}행의 데이터 삭제 완료'.format(result))
                
            # 변경사항 적용
            conn.commit()
            return result
        except pymysql.MySQLError as e:
            print("데이터 삭제 중 에러 발생 : ", e)
    # 데이터 수정 끝




# AddressBook 클래스 끝

# 객체 생성
my_app = AddressBook()

# 프로그램 실행 - run()
my_app.run()

