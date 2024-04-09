
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

name1 = input("조회할 이름 : ")

try:
    # 커서 생성
    with conn.cursor() as cursor:
        # 데이터 등록
        sql = " DELETE FROM 학생  "\
            + " WHERE name = %s "

        # result = cursor.execute(sql)          # 쿼리 실행 요청
        result = cursor.execute(sql, (name1))
        print('{}행의 데이터 삭제 완료'.format(result))
        
    # 변경사항 적용
    conn.commit()

except pymysql.MySQLError as e:
    print("데이터 등록 중 에러 발생 : ", e)
finally:
    conn.close()