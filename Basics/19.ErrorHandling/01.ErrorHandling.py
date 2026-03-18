# 错误处理

# 什么是错误处理？
# 使用try-except捕获和处理错误

# 基本用法
try:
    number = int(input("请输入数字: "))
    print(f"你输入的数字是: {number}")
except ValueError:
    print("输入的不是有效数字！")

# 多个异常
try:
    a = int(input("请输入第一个数字: "))
    b = int(input("请输入第二个数字: "))
    result = a / b
    print(f"{a} / {b} = {result}")
except ValueError:
    print("输入的不是有效数字！")
except ZeroDivisionError:
    print("不能除以零！")

# else和finally
try:
    number = int(input("请输入数字: "))
except ValueError:
    print("输入错误！")
else:
    print(f"输入正确: {number}")
finally:
    print("程序结束")

# 抛出异常
def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f"错误: {e}")
