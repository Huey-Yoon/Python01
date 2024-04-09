
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


std_id = input("변경 학번 : ")
name = input("변경 이름 : ")
tel = input("변경 전화번호 : ")

try:
    # 커서 생성
    with conn.cursor() as cursor:
        # 데이터 등록
        sql = " UPDATE 학생  "\
            + "   SET std_id = %s "\
            + "    , name = %s  "\
            + "    , tel = %s "\
            + "    , upd_date = now() "\
            + " WHERE name = %s "

        # result = cursor.execute(sql)          # 쿼리 실행 요청
        result = cursor.execute(sql, (std_id, name, tel, name1))
        print('{}행의 수정 완료'.format(result))
        
    # 변경사항 적용
    conn.commit()

except pymysql.MySQLError as e:
    print("데이터 등록 중 에러 발생 : ", e)
finally:
    conn.close()