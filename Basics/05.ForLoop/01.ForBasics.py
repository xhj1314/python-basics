# for循环基础

# 什么是for循环？
# for循环用于遍历一个序列（列表、元组、字符串等）中的每个元素

# 基本语法：
# for 变量 in 序列:
#     执行的代码

# 示例1：遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"水果: {fruit}")
print("\n")

# 示例2：遍历字符串
name = "Python"
for char in name:
    print(f"字符: {char}")
print("\n")

# 示例3：遍历元组
colors = ("红色", "绿色", "蓝色")
for color in colors:
    print(f"颜色: {color}")
print("\n")

# 示例4：遍历字典
student = {"name": "小明", "age": 18, "city": "北京"}
for key in student:
    print(f"键: {key}")
print("\n")

# 示例5：遍历字典的键值对
for key, value in student.items():
    print(f"{key}: {value}")

# 注意：
# 1. for后面的变量名可以自定义
# 2. 序列可以是列表、元组、字符串、字典等
# 3. 循环会依次处理序列中的每个元素
