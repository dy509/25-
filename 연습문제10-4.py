def input_scores():#Q1이렇게 인수가 없는 함수는 언제 쓰이는건지
    s=[]
    i=1
    while True:#Q2while True랑 뭐가 다른지??
        n=int(input(f'#{i}?'))
        if n<0:
            break
        s.append(n)
        i+=1
    return s

def get_average(s):
    total=0
    for n in s:
        total+=n
    return total/len(s)

def show_scores(s):
    for n in s:
        print(n,end=' ')
    print()

def search(lst,n):
    if n not in lst:
        return None
    return lst.index(n)

#주 프로그램부
print('[점수 입력]')
scores=input_scores()

print('\n[점수 출력]')
print('개인 점수:',end='')
show_scores(scores)

avg=get_average(scores)
print(f'평균:{avg:.2f}')

print('[검색]')
s=int(input('찾고자 하는 점수는? '))
if s in scores:
    idx=scores.index(s)#리스트에서 인덱스 찾기
    print(f'{s}점은 {idx+1}번 학생의 점수입니다.')
else:
    print(f'{s}점을 받은 학생은 없습니다.')