# 函数返回值

# 1. 无返回值
def say_hello():
    print("你好！")

result = say_hello()
print(f"返回值: {result}")  # None
print("\n")

# 2. 单个返回值
def square(x):
    return x ** 2

result = square(5)
print(f"5的平方: {result}")
print("\n")

# 3. 多个返回值
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print(f"最小值: {min_val}, 最大值: {max_val}")
print("\n")

# 4. 返回列表
def get_even_numbers(n):
    return [i for i in range(n) if i % 2 == 0]

evens = get_even_numbers(10)
print(f"偶数: {evens}")
print("\n")

# 5. 返回字典
def create_student(name, age):
    return {"name": name, "age": age}

student = create_student("小明", 18)
print(f"学生信息: {student}")
print("\n")

# 6. 提前返回
def is_positive(n):
    if n > 0:
        return True
    return False

print(f"5是正数: {is_positive(5)}")
print(f"-3是正数: {is_positive(-3)}")
