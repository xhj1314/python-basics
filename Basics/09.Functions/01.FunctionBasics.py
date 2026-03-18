# 函数基础

# 什么是函数？
# 函数是一段可重复使用的代码块，用于完成特定任务

# 基本语法：
# def 函数名(参数):
#     函数体
#     return 返回值

# 示例1：无参数无返回值的函数
def say_hello():
    print("你好！")

say_hello()  # 调用函数
print()

# 示例2：有参数无返回值的函数
def greet(name):
    print(f"你好, {name}!")

greet("小明")
print()

# 示例3：有参数有返回值的函数
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")
print()

# 示例4：多个返回值
def get_info():
    return "小明", 18

name, age = get_info()
print(f"姓名: {name}, 年龄: {age}")
print()

# 示例5：默认参数
def greet_with_title(name, title="先生"):
    print(f"{title} {name}")

greet_with_title("张三")
greet_with_title("李四", "女士")
print()

# 示例6：关键字参数
def introduce(name, age, city):
    print(f"姓名: {name}, 年龄: {age}, 城市: {city}")

introduce(age=20, name="小红", city="北京")
