#할인율 받기(전역변수)
#할인된 가격 입력받기
#정가 계산하기
#정가 출력하기

def get_fixed_price(pname):
    price=int(input(f"{pname}상품의 할인된 가격은?"))
    original_price=price/(1-dc/100)
    return(original_price)

#main
dc=int(input("할인율은?"))
first_res=int(get_fixed_price("A"))
sec_res=int(get_fixed_price("B"))
print(f"A상품의 정가는 {first_res}원 입니다")
print(f"B상품의 정가는 {sec_res}원 입니다")
