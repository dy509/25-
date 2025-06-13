def buy(sbag):
    print('[구입]')
    item=input('상품명은?')

    if item=='':
        return False

    price=int(input('수량은?'))

    sbag[item]=price
    print(f'장바구니에 {item} {price}개가 담겼습니다.\n')
    return True

def show(sbag):
    print('\n>>>장바구니 보기: ',end='')
    print(sbag)

def find(sbag):
    print('\n[검색]')
    item==input('장바구니에서 확인하고자 하는 상품은?')

    n=sbag.get(item)
    if n !=None:
        print(f'{item}은(는) {n}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {item}은(는) 없습니다.')

#주 프로그램부
shopping_bag={}

while True:
    if buy(shopping_bag)==False:
        break

show(shopping_bag)

find(shopping_bag)