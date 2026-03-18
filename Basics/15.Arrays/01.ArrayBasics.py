# 数组基础

# 什么是数组？
# Python没有内置数组，通常用列表代替
# 也可以使用array模块或numpy库

# 1. 使用列表作为数组
numbers = [1, 2, 3, 4, 5]
print(f"列表数组: {numbers}")
print("\n")

# 2. 使用array模块
import array

# 创建整数数组
int_array = array.array('i', [1, 2, 3, 4, 5])
print(f"整数数组: {int_array}")
print("\n")

# 3. 使用numpy（需要安装）
# import numpy as np
# np_array = np.array([1, 2, 3, 4, 5])
# print(f"numpy数组: {np_array}")

# 数组操作
numbers.append(6)       # 添加元素
numbers.remove(3)       # 删除元素
numbers[0] = 10         # 修改元素
print(f"修改后: {numbers}")
print("\n")

# 遍历数组
for num in numbers:
    print(num, end=" ")
print("\n")
