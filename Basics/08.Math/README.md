# 数学教程.md

# Python 数学教程 

## 1. 内置数学函数

Python内置了常用的数学函数：

```python
# 绝对值
abs(-5)  # 5

# 最大值和最小值
max(1, 2, 3)  # 3
min(1, 2, 3)  # 1

# 幂运算
pow(2, 3)  # 8

# 四舍五入
round(3.14159, 2)  # 3.14

# 求和
sum([1, 2, 3, 4, 5])  # 15
```

## 2. math模块

需要导入math模块：

```python
import math

# 圆周率
math.pi  # 3.141592653589793

# 平方根
math.sqrt(16)  # 4.0

# 向上取整和向下取整
math.ceil(3.2)   # 4
math.floor(3.8)  # 3

# 三角函数
math.sin(0)  # 0.0
math.cos(0)  # 1.0

# 阶乘
math.factorial(5)  # 120
```

## 3. 实践练习

```python
import math

# 计算圆的面积
radius = 5
area = math.pi * radius ** 2
print(f"圆的面积: {area:.2f}")

# 计算斜边长度
a, b = 3, 4
c = math.sqrt(a**2 + b**2)
print(f"斜边长度: {c}")
```

## 4. 总结

掌握常用的数学函数和math模块！