print('[점수 입력]')
scores=[]

for i in range (1,4):
    score=int(input(f'#{i}: '))
    scores.append(score)

avg=sum(scores)/len(scores)

print('[점수 출력]')
print('입력 점수: ',scores[0], scores[1], scores[2])
print(f'평균: {avg:.2f}' )

