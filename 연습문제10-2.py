def find_max(lst):#임의의 길이를 갖는 리스트를 입력받기
    m=lst[0]#리스트의 첫 번째 값을 초기 최대값으로 지정
    for i in range(1,len(lst)):#리스트의 두 번째부터 마지막까지 반복
        if lst[i]>m:#현재 리스트 값(lst[i])이 m보다 크면 더 큰 값을 찾은 거니까
            m=lst[i]#최대값을 새로 찾은 값으로 바꿔줌
    return m#함수를 호출한 코드 바깥에 돌려줘야 다른 코드에서 m을 쓸 수 있음

nums=[]

for i in range(5):
    n=int(input('정수 입력: '))#점수 입력을 5회 받음
    nums.append(n)#리스트에 점수 추가

print(f'가장 큰 정수는 {find_max(nums)}')

#사용자로부터 입력 받은 수 중에 가장 큰 수 찾기
