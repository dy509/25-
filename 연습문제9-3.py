shoppingBag = []  # 장바구니

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':  # 빈 문자열 입력하면 종료
        break
    shoppingBag.append(item)
    print(f'장바구니에 {item}가(이) 담겼습니다.')

# 최종 장바구니 출력
print(f'\n>>> 장바구니 보기: {shoppingBag}')
