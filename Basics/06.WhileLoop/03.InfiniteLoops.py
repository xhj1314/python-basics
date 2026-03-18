# 无限循环

# 什么是无限循环？
# 条件永远为True的循环，需要用break跳出

# 示例1：基本无限循环
print("基本无限循环:")
count = 0
while True:
    print(f"计数: {count}")
    count += 1
    if count >= 5:
        break
print("\n")

# 示例2：用户菜单
print("\n用户菜单:")
while True:
    print("\n=== 菜单 ===")
    print("1. 查看信息")
    print("2. 修改信息")
    print("3. 退出")
    
    choice = input("请选择(1-3): ")
    
    if choice == "1":
        print("查看信息")
    elif choice == "2":
        print("修改信息")
    elif choice == "3":
        print("退出系统")
        break
    else:
        print("无效选择，请重试")
print("\n")

# 示例3：读取输入直到有效
print("\n读取有效输入:")
while True:
    age = input("请输入年龄(1-120): ")
    if age.isdigit() and 1 <= int(age) <= 120:
        print(f"年龄: {age}")
        break
    else:
        print("无效输入，请重试")
print("\n")

# 示例4：重试机制
print("\n重试机制:")
max_attempts = 3
attempts = 0
while True:
    password = input("请输入密码: ")
    attempts += 1
    
    if password == "123456":
        print("登录成功！")
        break
    elif attempts >= max_attempts:
        print("尝试次数过多，账户已锁定")
        break
    else:
        print(f"密码错误，还有{max_attempts - attempts}次机会")
print("\n")

# 注意：无限循环必须有退出条件（break），否则程序会一直运行
