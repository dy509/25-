def input_scores():
    s=[]
    i=1
    while True:
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

#주 프로그램부
print('[점수 입력]')
scores=input_scores()

print('\n[점수 출력]')
print('개인 점수:',end='')
show_scores(scores)

avg=get_average(scores)
print(f'평균:{avg:.2f}')
