# f-string格式化

# 什么是f-string？
# f-string是Python 3.6+引入的字符串格式化方法，简单易用

# 基本语法：f"文本{变量}文本"

# 示例1：基本用法
name = "小明"
age = 18
print(f"姓名: {name}, 年龄: {age}")
print()

# 示例2：表达式计算
a = 10
b = 20
print(f"{a} + {b} = {a + b}")
print("\n")

# 示例3：格式化数字
price = 19.99
print(f"价格: {price:.2f}元")
print("\n")

# 示例4：格式化百分比
score = 85
print(f"得分率: {score / 100:.1%}")
print()

# 示例5：对齐
print(f"{'姓名':<10}{'年龄':>10}")
print(f"{name:<10}{age:>10}")
print()

# 示例6：调用函数
def get_greeting(name):
    return f"你好, {name}!"

print(f"问候: {get_greeting(name)}")
print("\n")

# 示例7：字典
student = {"name": "小红", "age": 20}
print(f"学生: {student['name']}, 年龄: {student['age']}")
