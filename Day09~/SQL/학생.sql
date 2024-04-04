SELECT * FROM joeun.학생;

-- 데이터 추가
INSERT INTO 학생 ( stu_id, name, tel )
VALUES ('A2404', '윤정현', '010-4511-9615');

-- 데이터 수정
UPDATE 학생
	SET name = '김조은'
WHERE stu_id = 'A2404'
    ;
    
-- 데이터 삭제
DELETE FROM 학생
WHERE name = '김조은';