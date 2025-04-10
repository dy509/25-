#영어로 된 이름을 입력 받아 두줄로 환영
#연습문제에 6.4, 6.5의 사용자 정의 함수 약간 변형
# 6.4->def rep_char(c,n): print(c,n)
#6.5-> def draw_line_string(msg): nstr=len(msg)/rep_char('-',nstr*2+4)/print(f'  {msg}  ')/rep_char('-',nstr*2+4)
#첫줄과 두번째줄 중 긴 줄 기준 박스선 길이 설정

#사용자 정의 함수부

def rep_char(c,n):
    print(c*n)

def draw_line_string(name):
    msg1=name
    msg2='Welcome_to_Seoul'
    nstr=len(msg1)if (len(msg1)>len(msg2))else len(msg2)

    rep_char('-',nstr)
    print(f'{msg1}\n{msg2}')
    rep_char('-',nstr)

#주 프로그램부
n= input('input his/her name:')
draw_line_string(n)