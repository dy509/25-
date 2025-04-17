#정수를 입력
#한글로 읽어줌


#사용자 정의 함수부
def read_single_digit(digit):
    names=["공","일","이","삼","사","오","육","칠","팔","구"]
    return names[digit]    

def read_number(digit):
    a= digit // 100
    b = (digit % 100) // 10
    c= digit % 10

    print(read_single_digit(a)+read_single_digit(b)+read_single_digit(c))

#주프로그램부
number=int(input('세 자리 정수 입력'))
read_number(number)
