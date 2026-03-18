# 循环控制

# 什么是循环控制？
# 使用break、continue、pass控制循环的执行

# 1. break - 跳出整个循环
print("break示例:")
for i in range(10):
    if i == 5:
        print("遇到5，跳出循环")
        break
    print(f"数字: {i}")
print("\n")

# 2. continue - 跳过本次循环，继续下一次
print("\ncontinue示例:")
for i in range(10):
    if i % 2 == 0:  # 跳过偶数
        continue
    print(f"奇数: {i}")
print("\n")

# 3. pass - 占位符，什么都不做
print("\npass示例:")
for i in range(5):
    if i == 2:
        pass  # 暂时不处理
    print(f"数字: {i}")
print("\n")

# 4. else - 循环正常结束后执行
print("\nelse示例:")
for i in range(5):
    print(f"数字: {i}")
else:
    print("循环正常结束")
print("\n")

# 5. else和break配合
print("\nelse和break示例:")
for i in range(10):
    if i == 3:
        print("找到3，跳出循环")
        break
    print(f"数字: {i}")
else:
    print("循环正常结束（不会执行）")
print("\n")

# 示例：查找元素
print("\n查找元素示例:")
fruits = ["苹果", "香蕉", "橙子"]
target = "香蕉"
for fruit in fruits:
    if fruit == target:
        print(f"找到了: {fruit}")
        break
else:
    print(f"没有找到: {target}")
