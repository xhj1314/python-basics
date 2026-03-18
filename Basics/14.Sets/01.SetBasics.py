# 集合基础

# 什么是集合？
# 集合是一个无序的、不重复的元素集合

# 创建集合
fruits = {"苹果", "香蕉", "橙子"}
print(f"水果集合: {fruits}")
print()

# 创建空集合
empty_set = set()  # 注意：不能用{}，那是空字典

# 添加元素
fruits.add("葡萄")
print(f"添加后: {fruits}")
print()

# 删除元素
fruits.remove("香蕉")
print(f"删除后: {fruits}")
print()

# 集合运算
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"并集: {a | b}")      # {1, 2, 3, 4, 5, 6}
print(f"交集: {a & b}")      # {3, 4}
print(f"差集: {a - b}")      # {1, 2}
print(f"对称差: {a ^ b}")     # {1, 2, 5, 6}
print()

# 去重
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(f"去重后: {unique}")
