# range函数

# 什么是range函数？
# range函数用于生成一个数字序列，常用于for循环

# 基本语法：
# range(stop)              # 从0到stop-1
# range(start, stop)       # 从start到stop-1
# range(start, stop, step) # 从start到stop-1，步长为step

# 示例1：基本用法
for i in range(5):
    print(f"数字: {i}")  # 输出: 0, 1, 2, 3, 4
print("\n")

# 示例2：指定起始和结束
for i in range(1, 6):
    print(f"数字: {i}")  # 输出: 1, 2, 3, 4, 5
print("\n")

# 示例3：指定步长
for i in range(0, 10, 2):
    print(f"偶数: {i}")  # 输出: 0, 2, 4, 6, 8
print("\n")

# 示例4：倒序
for i in range(5, 0, -1):
    print(f"倒计时: {i}")  # 输出: 5, 4, 3, 2, 1
print("\n")

# 示例5：计算1到100的和
total = 0
for i in range(1, 101):
    total += i
print(f"1到100的和: {total}")
print("\n")

# 示例6：打印乘法表的一行
n = 5
for i in range(1, 10):
    print(f"{n} × {i} = {n * i}")
print("\n")

# 示例7：遍历列表的索引
fruits = ["苹果", "香蕉", "橙子"]
for i in range(len(fruits)):
    print(f"{i + 1}. {fruits[i]}")
