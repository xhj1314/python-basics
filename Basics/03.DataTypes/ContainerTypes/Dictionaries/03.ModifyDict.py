# 修改字典

# 创建字典
student = {
    "name": "小明",
    "age": 18,
    "city": "北京"
}
print("原始字典:", student)

# 1. 修改值
student["age"] = 19  # 修改年龄
print("修改年龄后:", student)

# 2. 添加新的键值对
student["gender"] = "男"  # 添加性别
print("添加性别后:", student)

# 3. 删除键值对
del student["city"]  # 删除城市
print("删除城市后:", student)

# 4. 使用pop()删除并返回值
age = student.pop("age")  # 删除年龄并返回它
print("删除的年龄:", age)
print("删除年龄后:", student)

# 5. 清空字典
temp_dict = {"a": 1, "b": 2}
print("\n临时字典:", temp_dict)
temp_dict.clear()
print("清空后:", temp_dict)

# 6. 批量更新字典
student = {
    "name": "小明",
    "age": 18
}
student.update({"city": "北京", "gender": "男"})
print("批量更新后:", student)
