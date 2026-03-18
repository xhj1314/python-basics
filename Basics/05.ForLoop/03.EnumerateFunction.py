# enumerate函数

# 什么是enumerate函数？
# enumerate函数用于同时获取索引和元素

# 基本语法：
# for index, value in enumerate(序列):
#     执行的代码

# 示例1：基本用法
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")
print("\n")

# 示例2：指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
print("\n")

# 示例3：遍历字符串
name = "Python"
for index, char in enumerate(name):
    print(f"位置{index}: {char}")
print("\n")

# 示例4：遍历字典
student = {"name": "小明", "age": 18, "city": "北京"}
for index, (key, value) in enumerate(student.items()):
    print(f"{index + 1}. {key}: {value}")
print("\n")

# 示例5：查找元素的索引
fruits = ["苹果", "香蕉", "橙子", "香蕉", "葡萄"]
target = "香蕉"
for index, fruit in enumerate(fruits):
    if fruit == target:
        print(f"找到{target}，索引: {index}")
print("\n")

# 示例6：同时遍历多个列表
names = ["小明", "小红", "小刚"]
ages = [18, 19, 20]
for index, name in enumerate(names):
    print(f"{name}的年龄是{ages[index]}")
print("\n")

# 示例7：使用zip和enumerate
for index, (name, age) in enumerate(zip(names, ages)):
    print(f"{index + 1}. {name}: {age}岁")
