# format方法

# 什么是format方法？
# format方法是字符串的内置方法，用于格式化字符串

# 基本语法："文本{}文本".format(值)

# 示例1：基本用法
name = "小明"
age = 18
print("姓名: {}, 年龄: {}".format(name, age))
print("\n")

# 示例2：位置参数
print("{0} {1} {0}".format("Hello", "World"))
print("\n")

# 示例3：关键字参数
print("姓名: {name}, 年龄: {age}".format(name="小红", age=20))
print("\n")

# 示例4：格式化数字
price = 19.99
print("价格: {:.2f}元".format(price))
print("\n")

# 示例5：格式化百分比
score = 85
print("得分率: {:.1%}".format(score / 100))
print("\n")

# 示例6：对齐
print("{:<10}{:>10}".format("姓名", "年龄"))
print("{:<10}{:>10}".format(name, age))
print("\n")

# 示例7：填充
print("{:*^20}".format("居中"))
