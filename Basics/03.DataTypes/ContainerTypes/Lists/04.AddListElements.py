# 添加列表元素

# 列表是可变的，可以随时添加新元素

# 创建一个列表
fruits = ["苹果", "香蕉"]
print("原始列表:", fruits)

# 方法1：在末尾添加一个元素（最常用）
fruits.append("橙子")
print("append添加后:", fruits)  # 输出: ['苹果', '香蕉', '橙子']

# 方法2：在指定位置插入元素
fruits.insert(1, "梨")  # 在索引1的位置插入"梨"
print("insert插入后:", fruits)  # 输出: ['苹果', '梨', '香蕉', '橙子']

# 方法3：在末尾添加多个元素
fruits.extend(["葡萄", "西瓜"])
print("extend添加后:", fruits)  # 输出: ['苹果', '梨', '香蕉', '橙子', '葡萄', '西瓜']

# 方法4：使用 + 合并两个列表
more_fruits = ["柠檬", "桃子"]
all_fruits = fruits + more_fruits
print("合并后的列表:", all_fruits)

# 示例：逐步构建列表
shopping_list = []  # 从空列表开始
print("\n购物清单:", shopping_list)

shopping_list.append("牛奶")
print("添加牛奶后:", shopping_list)

shopping_list.append("面包")
print("添加面包后:", shopping_list)

shopping_list.append("鸡蛋")
print("添加鸡蛋后:", shopping_list)

# 总结：
# append() - 在末尾添加一个元素（最常用）
# insert() - 在指定位置插入元素
# extend() - 在末尾添加多个元素
# + - 合并两个列表，创建新列表
