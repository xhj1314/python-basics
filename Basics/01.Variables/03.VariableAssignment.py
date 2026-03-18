# 变量赋值

# 1. 单个变量赋值
x = 10
print("x =", x)  # 输出: x = 10

# 2. 多个变量赋相同的值
a = b = c = 0
print("a =", a, "b =", b, "c =", c)  # 输出: a = 0 b = 0 c = 0

# 3. 多个变量赋不同的值
x, y, z = 1, 2, 3
print("x =", x, "y =", y, "z =", z)  # 输出: x = 1 y = 2 z = 3

# 4. 交换两个变量的值
a = 10
b = 20
print("交换前: a =", a, "b =", b)
a, b = b, a  # 交换
print("交换后: a =", a, "b =", b)

# 5. 变量可以重新赋值
name = "小明"
print("第一次:", name)
name = "小红"  # 重新赋值
print("第二次:", name)
name = 100     # 甚至可以改变类型
print("第三次:", name)
