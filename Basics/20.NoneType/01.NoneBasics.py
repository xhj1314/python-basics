# None基础

# 什么是None？
# None表示"无"或"空"，是Python的特殊值

# 创建None变量
x = None
print(f"x的值: {x}")
print()

# 检查是否为None
if x is None:
    print("x是None")
print()

# 函数默认返回None
def my_function():
    pass

result = my_function()
print(f"函数返回值: {result}")  # None
print()

# None在条件判断中
if not None:
    print("None是False")
print()

# None作为默认参数
def greet(name=None):
    if name is None:
        name = "陌生人"
    print(f"你好, {name}!")

greet()
greet("小明")
