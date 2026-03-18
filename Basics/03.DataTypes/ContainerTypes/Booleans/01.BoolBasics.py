# 布尔值的基本定义

# 定义布尔值变量
is_active = True    # 真
is_admin = False   # 假

# 打印布尔值
print("is_active =", is_active)  # 输出: is_active = True
print("is_admin =", is_admin)    # 输出: is_admin = False

# 布尔值的特点

# ✅ 首字母大写：True 和 False 是 Python 关键字，必须首字母大写
# 错误示例：true、false（小写）会导致语法错误

# ✅ 本质是 int 的子类：
# True 等价于 1
# False 等价于 0

# 示例：布尔值与整数的运算（虽然不常用，但有助于理解）
print("True + 1 =", True + 1)   # 输出: 2（因为 True == 1）
print("False * 10 =", False * 10) # 输出: 0（因为 False == 0）
print("True == 1 =", True == 1)  # 输出: True
print("False == 0 =", False == 0)  # 输出: True