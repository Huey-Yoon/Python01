# 아래의 [보기]의 주어진 코드를 활용하여, 다음 요구사항에 따라 출력결과와 일치하는 코드를 완성하시오.

# 보기
def getStudent(no, name, major):
    # TODO: 함수를 완성하시오
    getStudent = [no, name, major]
    return getStudent

no = input('학번 : ')
name = input('이름 : ')
major = input('전공명 : ')

student = getStudent(no, name, major)

# TODO: 출력문 내부를 완성하시오.
print('학번 :',student[0])
print('이름 :',student[1])
print('전공명 :',student[2])