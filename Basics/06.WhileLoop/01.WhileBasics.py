# while循环基础

# 什么是while循环？
# while循环在条件为True时重复执行代码块

# 基本语法：
# while 条件:
#     执行的代码

# 示例1：基本用法
count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1
print("\n")

# 示例2：计算1到100的和
total = 0
num = 1
while num <= 100:
    total += num
    num += 1
print(f"1到100的和: {total}")
print("\n")

# 示例3：倒计时
countdown = 5           # 初始值设为5
while countdown > 0:    # 当 countdown 大于 0 时循环
    print(f"倒计时: {countdown}")  # 打印当前倒计时数字
    countdown -= 1      # 每次循环减1
print("发射！")         # 循环结束后打印"发射！"
print("\n")             # 打印空行分隔

# 示例4：用户输入验证
password = ""
while password != "123456":
    password = input("请输入密码: ")
print("密码正确！")
print("\n")

# 示例5：遍历列表
fruits = ["苹果", "香蕉", "橙子"]
index = 0
while index < len(fruits):
    print(f"水果: {fruits[index]}")
    index += 1

# 注意：
# 1. 条件必须最终变为False，否则会无限循环
# 2. 循环体内要更新条件变量
# 3. 小心无限循环
