# 3️⃣ 列表的遍历
# 使用 for循环 循环遍历所有元素：

fruits = ["苹果", "香蕉", "橙子", "葡萄"]
numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", True, [5, 6]]  # 混合类型
# 直接遍历元素
for fruit in fruits:
    print(fruit)

# 遍历索引和元素（推荐）
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")