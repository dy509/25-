print('[점수 입력]')
student1=int(input('#1: '))
student2=int(input('#2: '))
student3=int(input('#3: '))

scores=[]
scores.append(student1)
scores.append(student2)
scores.append(student3)

avg=(scores[0]+scores[1]+scores[2])/3

print('[점수 출력]')
print('입력 점수: ',scores[0], scores[1], scores[2])
print(f'평균: {avg:.2f}' )

print('[검색]')
findScore=int(input('찾고자 하는 점수는? '))
if findScore in scores:
    print(f'{findScore}점은 {scores.index(findScore)+1}번 학생의 점수입니다.')
else:
    print(f'{findScore}점은 존재하지 않습니다.')