# 类基础

# 什么是类？
# 类是对象的模板，定义了对象的属性和方法

# 定义类
class Person:
    def __init__(self, name, age):
        self.name = name  # 属性
        self.age = age
    
    def introduce(self):  # 方法
        print(f"我叫{self.name}, 今年{self.age}岁")

# 创建对象
person1 = Person("小明", 18)
person2 = Person("小红", 20)

# 调用方法
person1.introduce()
person2.introduce()
print("\n")

# 访问属性
print(f"姓名: {person1.name}")
print(f"年龄: {person1.age}")
print("\n")

# 修改属性
person1.age = 19
print(f"新年龄: {person1.age}")
