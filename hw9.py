# Point 클래스 정의
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f"({self.__x}, {self.__y})", end=" ")

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def get(self):
        return (self.__x, self.__y)

    def toString(self):
        return f"({self.__x}, {self.__y})"

# Rectangle 클래스 정의
class Rectangle:
    def __init__(self, lt_x, lt_y, rb_x, rb_y):
        self.lt_x = lt_x
        self.lt_y = lt_y
        self.lt = Point(lt_x, lt_y)
        self.rb = Point(rb_x, rb_y)

    def show(self):
        print(f"좌 상단 좌표값이 {self.lt.toString()}이고 ", end="")
        print(f"우 하단 좌표값이 {self.rb.toString()}인 사각형입니다.", end="")

    def getWidth(self):
        return self.rb.getX() - self.lt.getX()

    def getHeight(self):
        return self.rb.getY() - self.lt.getY()

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return (self.getWidth() + self.getHeight()) * 2

# 테스트 코드
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f"\n넓이는 {a}, 둘레는 {p}")
