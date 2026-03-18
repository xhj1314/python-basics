# 访问字典元素

# 创建字典
student = {
    "name": "小明",
    "age": 18,
    "city": "北京"
}

# 方法1：通过键访问值
print("姓名:", student["name"])    # 输出: 小明
print("年龄:", student["age"])      # 输出: 18
print("城市:", student["city"])     # 输出: 北京

# 方法2：使用get()方法（推荐）
# 如果键不存在，不会报错，可以返回默认值
print("姓名:", student.get("name"))           # 输出: 小明
print("性别:", student.get("gender", "未知"))  # 输出: 未知

# 注意：如果键不存在，使用[]会报错
# print(student["gender"])  # 错误！KeyError

# 获取所有键
keys = student.keys()
print("所有键:", list(keys))  # 输出: ['name', 'age', 'city']

# 获取所有值
values = student.values()
print("所有值:", list(values))  # 输出: ['小明', 18, '北京']

# 获取所有键值对
items = student.items()
print("所有键值对:", list(items))  # 输出: [('name', '小明'), ('age', 18), ('city', '北京')]
