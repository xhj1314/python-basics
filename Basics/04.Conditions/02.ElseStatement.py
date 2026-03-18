# else语句

# 什么是else语句？
# else语句用于在if条件不成立时执行的代码

# 基本语法：
# if 条件:
#     条件成立时执行
# else:
#     条件不成立时执行

# 示例1：判断是否成年
age = 15
if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")

# 示例2：判断奇偶数
number = 7
if number % 2 == 0:
    print(f"{number}是偶数")
else:
    print(f"{number}是奇数")

# 示例3：判断是否及格
score = 55
if score >= 60:
    print("及格了")
else:
    print("不及格，需要补考")

# 示例4：判断是否为空
name = ""
if name:
    print(f"名字是: {name}")
else:
    print("名字为空")

# 示例5：比较两个数字
a = 30
b = 20
if a > b:
    print("a比b大")
else:
    print("a不比b大")
