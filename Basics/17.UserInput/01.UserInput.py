# 用户输入

# 什么是用户输入？
# 使用input()函数获取用户输入

# 基本用法
name = input("请输入你的名字: ")
print(f"你好, {name}!")

# 输入数字（注意：input返回字符串）
age_str = input("请输入你的年龄: ")
age = int(age_str)  # 转换为整数
print(f"你明年{age + 1}岁")

# 输入浮点数
height = float(input("请输入你的身高(米): "))
print(f"你的身高是{height}米")

# 多个输入
a, b = input("请输入两个数字(用空格分隔): ").split()
a, b = int(a), int(b)
print(f"{a} + {b} = {a + b}")

# 输入验证
while True:
    password = input("请输入密码: ")
    if password == "123456":
        print("密码正确！")
        break
    else:
        print("密码错误，请重试")
