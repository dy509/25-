shopping_bag=[]
item_amount=[]

print('[구입]')
while True:
    item=input('상품명?')
    if item=='':
        break

    amount=input('수량은?')
    if amount=='':
        break


    shopping_bag.append(item)
    item_amount.append(amount)
    print(f'장바구니에 {item} {amount}개가 담겼습니다.')

# shopping_bag에 사용자로부터 입력받은 상품명과 수량을 저장
def buy(shopping_bag):
    print("[구입]")

    item = input("상품명? ")
    if item == "":
        return False

    amount = input("수량은? ")
    if amount == "":
        return False

    shopping_bag[item] = shopping_bag.get(item, 0) + int(amount)
    print(f"장바구니에 {item} {amount}개가 담겼습니다.")
    return True

# 장바구니에 들어 있는 전체 상품을 출력
def show(shopping_bag):
    print("\n>>> 장바구니 보기:")
    for item, amount in shopping_bag.items():
        print(f"{item}: {amount}개")

# 이 상품의 수량을 출력
def find(shopping_bag):
    print("\n[검색]")
    item = input("장바구니에서 확인하고자 하는 상품은? ")
    if item in shopping_bag:
        print(f"{item}은(는) {shopping_bag[item]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {item}은(는) 없습니다.")

#주프로그램부
shopping_bag={}
while True:
    if buy(shopping_bag)==False:
        break

show(shopping_bag)
find(shopping_bag )