# 浮点数

# 什么是浮点数？
# 浮点数是带有小数部分的数字

# 创建浮点数变量
pi = 3.14          # 正浮点数
temperature = -0.5  # 负浮点数
scientific = 2.5e3  # 科学计数法（2500.0）

# 打印浮点数
print("浮点数示例:", pi, temperature, scientific)

# 浮点数可以进行算术运算
print("\n算术运算:")
print("pi + 1 =", pi + 1)           # 加法: 3.14 + 1 = 4.14
print("temperature * 2 =", temperature * 2)  # 乘法: -0.5 * 2 = -1.0
print("scientific / 100 =", scientific / 100)  # 除法: 2500.0 / 100 = 25.0

# 注意：浮点数可能有精度问题
result = 0.1 + 0.2
print("\n0.1 + 0.2 =", result)  # 可能不是精确的0.3
