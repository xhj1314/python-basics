# 类型转换

# 什么是类型转换？
# 将一种数字类型转换为另一种数字类型

# 1. 转换为整数
x = int(3.9)    # 3（直接截断小数）
print("int(3.9) =", x)

y = int("10")   # 10（从字符串转换）
print("int('10') =", y)

# 2. 转换为浮点数
a = float(5)    # 5.0
print("float(5) =", a)

b = float("3.14")  # 3.14
print("float('3.14') =", b)

# 3. 转换为复数
z = complex(2)  # (2+0j)
print("complex(2) =", z)

w = complex(3, 4)  # (3+4j)
print("complex(3, 4) =", w)

# 注意：int()会直接截断小数，不是四舍五入
