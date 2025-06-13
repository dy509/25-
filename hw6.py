#2~5단에 대한 구구단표를 출력
for i in range(1,10):
    for n in range(2,6):
        print(f'{n}x{i}={n*i:2d}',end='\t')
    print()
print()
#6~9단에 대한 구구단표를 출력
for i in range(1,10):
    for n in range(6,10):
        print(f'{n}x{i}={n*i:2d}',end='\t')
    print()