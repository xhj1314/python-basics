# if语句基础

# 什么是if语句？
# if语句用于判断条件是否成立，如果成立就执行相应的代码

# 基本语法：
# if 条件:
#     执行的代码

# 示例1：简单的if语句
age = 18
if age >= 18:
    print("你已经成年了")

# 示例2：比较两个数字
a = 10
b = 20
if b > a:
    print("b比a大")

# 示例3：判断是否为正数
number = 5
if number > 0:
    print(f"{number}是正数")

# 示例4：判断字符串是否为空
name = "小明"
if name:
    print(f"名字是: {name}")

# 示例5：判断列表是否为空
fruits = ["苹果", "香蕉"]
if fruits:
    print(f"有{len(fruits)}个水果")

# 注意：
# 1. if后面的条件必须是布尔值（True或False）
# 2. 条件后面要加冒号:
# 3. 执行的代码要缩进（通常是4个空格）
