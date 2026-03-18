# 布尔值的常用方法

# 布尔值的基本操作

# 1. 算术运算
# 虽然 bool 类型是 int 的子类，支持部分数值操作，但通常不建议这样使用
# 因为布尔值主要用于逻辑判断

print("True + False =", True + False)  # 输出: 1（因为 True=1, False=0）
print("True * 5 =", True * 5)        # 输出: 5（因为 True=1）
print("False * 5 =", False * 5)      # 输出: 0（因为 False=0）

# 2. 比较操作
# 布尔值之间也可以比较
print("True == True =", True == True)  # 输出: True
print("True == False =", True == False)  # 输出: False
print("True > False =", True > False)    # 输出: True（因为 1 > 0）

# 3. 逻辑操作
# 布尔值的主要用途是逻辑操作
# 详细的逻辑运算见布尔值的来源.py