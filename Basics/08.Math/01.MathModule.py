# math模块

# 导入math模块
import math

# 1. 圆周率
print("圆周率:")
print(math.pi)  # 3.141592653589793

# 2. 向上取整和向下取整
print("\n取整:")
print(math.ceil(3.2))   # 4 (向上取整)
print(math.floor(3.8))  # 3 (向下取整)

# 3. 平方根
print("\n平方根:")
print(math.sqrt(16))  # 4.0

# 4. 幂运算
print("\n幂运算:")
print(math.pow(2, 3))  # 8.0

# 5. 三角函数
print("\n三角函数:")
print(math.sin(0))      # 0.0
print(math.cos(0))      # 1.0
print(math.tan(0))      # 0.0

# 6. 对数
print("\n对数:")
print(math.log(10))     # 自然对数
print(math.log10(100))  # 以10为底的对数

# 7. 阶乘
print("\n阶乘:")
print(math.factorial(5))  # 120

# 8. 判断是否为有限数
print("\n判断:")
print(math.isfinite(10))     # True
print(math.isinf(float('inf')))  # True
print(math.isnan(float('nan')))  # True
