shoppingBag = {} 

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':  
        break
    amount = input('수량은? ')
    shoppingBag [item]=amount #딕셔너리를 사용해서 수량 저장
    print(f'장바구니에 {item} {amount}개가 담겼습니다.')
    
print(f'\n>>> 장바구니 보기: {shoppingBag}')

print('[검색]')
findProduct=input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{findProduct}은(는) {shoppingBag[findProduct]}개 담겨 있습니다.')