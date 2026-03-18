# 继承基础

# 什么是继承？
# 继承允许一个类获得另一个类的属性和方法

# 父类
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name}发出声音")

# 子类继承父类
class Dog(Animal):
    def speak(self):  # 重写方法
        print(f"{self.name}汪汪汪")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}喵喵喵")

# 创建对象
dog = Dog("小黄")
cat = Cat("小白")

dog.speak()  # 小黄汪汪汪
cat.speak()  # 小白喵喵喵
print("\n")

# 使用super()调用父类方法
class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # 调用父类的__init__
        self.color = color
    
    def speak(self):
        super().speak()  # 调用父类的方法
        print(f"{self.name}叽叽喳喳")

bird = Bird("小鸟", "蓝色")
bird.speak()
