import math

def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    area=math.pi*radius**2
    return area

def main():
    radius=get_radius("원의 반지름을 압력하세요:")
    area=get_circle_area(radius)
    print(f"반지름이 {radius}인 원의 넓이는 {area:.2f}입니다.")  
