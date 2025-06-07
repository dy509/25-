def buy(shopping_bag):
    print('[구입]')
    while True:
        item = input('상품명? ')
        if item == '':
            return False  # 종료 신호
        amount = input('수량은? ')
        shopping_bag[item] = amount
        print(f'장바구니에 {item} {amount}개가 담겼습니다.')
    return True


def show(shopping_bag):
    print(f'\n>>> 장바구니 보기: {shopping_bag}')

def find(shopping_bag):
    print('[검색]')
    item = input('장바구니에서 확인하고자 하는 상품은? ')
    if item in shopping_bag:
        print(f'{item}은(는) {shopping_bag[item]}개 담겨 있습니다.')
    else:
        print(f'{item}은(는) 장바구니에 없습니다.')


# 주 프로그램
shopping_bag = {}
while True:
    if not buy(shopping_bag):
        break

show(shopping_bag)
find(shopping_bag)
