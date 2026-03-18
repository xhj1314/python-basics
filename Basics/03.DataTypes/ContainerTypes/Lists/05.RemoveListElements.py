# 删除列表元素

# 列表是可变的，可以删除不需要的元素

# 创建一个列表
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
print("原始列表:", fruits)

# 方法1：删除指定值的元素（只删除第一个匹配的）
fruits.remove("橙子")
print("remove删除橙子后:", fruits)  # 输出: ['苹果', '香蕉', '葡萄', '西瓜']

# 方法2：删除指定索引的元素，并返回被删除的元素
popped = fruits.pop(1)  # 删除索引1的元素（香蕉）
print("pop删除的元素:", popped)  # 输出: 香蕉
print("pop删除后:", fruits)  # 输出: ['苹果', '葡萄', '西瓜']

# 方法3：删除最后一个元素（不指定索引）
last = fruits.pop()
print("pop删除的最后一个元素:", last)  # 输出: 西瓜
print("pop删除后:", fruits)  # 输出: ['苹果', '葡萄']

# 方法4：使用del语句删除指定索引的元素
del fruits[0]
print("del删除后:", fruits)  # 输出: ['葡萄']

# 方法5：清空整个列表
fruits.clear()
print("clear清空后:", fruits)  # 输出: []

# 示例：删除重复元素
numbers = [1, 2, 3, 2, 4, 2, 5]
print("\n原始数字列表:", numbers)

# remove只删除第一个匹配的元素
numbers.remove(2)
print("remove删除第一个2后:", numbers)  # 输出: [1, 3, 2, 4, 2, 5]

# 总结：
# remove(值) - 删除指定值的第一个元素
# pop(索引) - 删除指定索引的元素，并返回它
# pop() - 删除最后一个元素，并返回它
# del 列表[索引] - 删除指定索引的元素
# clear() - 清空整个列表
