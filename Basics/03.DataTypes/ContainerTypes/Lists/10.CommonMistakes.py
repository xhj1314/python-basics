# 5️⃣ 常见错误
# ❗ 错误1：索引越界
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", True, [5, 6]]  # 混合类型
print(fruits[10])  # IndexError: list index out of range
# 解决方法：确保索引在 0 到 len(list)-1 范围内。

# ❗ 错误2：修改不可变对象的引用
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", True, [5, 6]]  # 混合类型
nested = [[1,2], [3,4]]
nested[0] = 5       # 正确：修改外层列表元素
nested[1][0] = 100  # 正确：修改内层列表元素
print("\n")