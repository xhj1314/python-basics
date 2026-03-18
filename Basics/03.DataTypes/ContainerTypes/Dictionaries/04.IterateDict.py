# 遍历字典

# 创建字典
student = {
    "name": "小明",
    "age": 18,
    "city": "北京"
}

# 1. 遍历所有键
print("遍历所有键:")
for key in student:
    print("键:", key)

# 或者使用keys()方法
print("\n使用keys()方法:")
for key in student.keys():
    print("键:", key)

# 2. 遍历所有值
print("\n遍历所有值:")
for value in student.values():
    print("值:", value)

# 3. 遍历所有键值对（推荐）
print("\n遍历所有键值对:")
for key, value in student.items():
    print(f"{key}: {value}")

# 4. 带索引遍历
print("\n带索引遍历:")
for index, (key, value) in enumerate(student.items()):
    print(f"{index + 1}. {key}: {value}")
