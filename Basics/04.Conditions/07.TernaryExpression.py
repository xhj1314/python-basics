# 三元表达式

# 什么是三元表达式？
# 三元表达式是if-else的简写形式，用于简单的条件判断

# 基本语法：
# 值1 if 条件 else 值2

# 示例1：判断是否成年
age = 20
status = "成年" if age >= 18 else "未成年"
print(f"状态: {status}")

# 示例2：判断奇偶数
number = 7
result = "偶数" if number % 2 == 0 else "奇数"
print(f"{number}是{result}")

# 示例3：判断及格
score = 75
grade = "及格" if score >= 60 else "不及格"
print(f"成绩: {grade}")

# 示例4：获取较大值
a = 10
b = 20
max_value = a if a > b else b
print(f"较大值: {max_value}")

# 示例5：获取绝对值
number = -5
absolute = number if number >= 0 else -number
print(f"{number}的绝对值是{absolute}")

# 示例6：设置默认值
name = ""
display_name = name if name else "匿名用户"
print(f"显示名称: {display_name}")

# 示例7：在打印中使用
score = 85
print("通过" if score >= 60 else "未通过")

# 注意：
# 1. 三元表达式适合简单的条件判断
# 2. 如果逻辑复杂，建议使用普通的if-else
# 3. 不要嵌套太多三元表达式，影响可读性
