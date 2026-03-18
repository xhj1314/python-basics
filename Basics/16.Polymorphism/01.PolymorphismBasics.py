# 多态基础

# 什么是多态？
# 多态是指不同的对象对同一方法有不同的响应

# 示例：动物叫声
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵喵"

# 多态：不同的对象调用同一方法，产生不同结果
def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_speak(dog)  # 汪汪汪
animal_speak(cat)  # 喵喵喵
print("\n")

# 示例：形状面积
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"矩形面积: {rectangle.area():.2f}")
print(f"圆形面积: {circle.area():.2f}")
print("\n")
