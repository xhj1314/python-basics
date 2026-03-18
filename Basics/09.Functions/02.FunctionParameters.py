# 函数参数

# 1. 位置参数
def add(a, b):
    return a + b

print("位置参数:", add(3, 5))
print("\n")

# 2. 关键字参数
def greet(name, age):
    print(f"姓名: {name}, 年龄: {age}")

greet(age=18, name="小明")
print("\n")

# 3. 默认参数
def greet_with_city(name, city="北京"):
    print(f"姓名: {name}, 城市: {city}")

greet_with_city("小红")
greet_with_city("小刚", "上海")
print("\n")

# 4. 可变位置参数 (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("可变位置参数:", sum_all(1, 2, 3, 4, 5))
print("\n")

# 5. 可变关键字参数 (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="小明", age=18, city="北京")
print("\n")

# 6. 组合使用
def func(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, name="小红", age=20)
