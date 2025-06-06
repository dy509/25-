#1~4층의 거주인원수를 받음
def input_num_of_population():
    nPeople=[]
    for f in range(4):
        n=int(input(f'{f+1}층의 거주인원수는?'))
        nPeople.append(n)
    return nPeople

#입력받음 1~4층의 거주인원수를 출력
def show_num_of_population(p):
    f=1
    for n in p:
        print(f'{f}층의 거주인원수는 {n}명입니다')
        f+=1

#total=입력받은 1~4층의 거주인원수의 총합을 구함
def get_total(lst):
    total=0
    for n in lst:
        total+=n
    return total

#주 프로그램부
#1~4층의 거주인원수를 받음
population=input_num_of_population()
#입력받은 1~4층의 거주인원수를 출력
print('\n')
show_num_of_population(population)
#total=입력받은 1~4층의 거주인원수의 총합을 구함
total=get_total(population)
#총 거주인원수(total)출력
print(f'\n총 거주인원수는 {total}명입니다.')
