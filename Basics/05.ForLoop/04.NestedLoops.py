# 嵌套循环

# 什么是嵌套循环？
# 在一个循环内部再使用一个循环

# 示例1：打印矩形
print("打印矩形:")
for i in range(3):  # 行
    for j in range(5):  # 列
        print("*", end="")
    print()  # 换行
print("\n")

# 示例2：打印直角三角形
print("\n打印直角三角形:")
for i in range(1, 6):  # 行数
    for j in range(i):  # 每行的星号数
        print("*", end="")
    print()
print("\n")

# 示例3：打印九九乘法表
print("\n九九乘法表:")
for i in range(1, 10):  # 行
    for j in range(1, i + 1):  # 列
        print(f"{j}×{i}={i*j}", end="\t")
    print()
print("\n")

# 示例4：遍历二维列表
print("\n遍历二维列表:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
print("\n")

# 示例5：查找二维列表中的元素
print("\n查找元素:")
target = 5
found = False
for i, row in enumerate(matrix):
    for j, num in enumerate(row):
        if num == target:
            print(f"找到{target}，位置: ({i}, {j})")
            found = True
            break
    if found:
        break
print("\n")

# 示例6：组合遍历
print("\n组合遍历:")
colors = ["红色", "绿色", "蓝色"]
sizes = ["S", "M", "L"]
for color in colors:
    for size in sizes:
        print(f"{color} - {size}")
