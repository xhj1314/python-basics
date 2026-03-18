# 比较运算符

# 什么是比较运算符？
# 用于比较两个值，返回True或False

# 1. 等于 ==
a = 5
b = 5
if a == b:
    print("a等于b")

# 2. 不等于 !=
c = 10
d = 20
if c != d:
    print("c不等于d")

# 3. 大于 >
e = 15
f = 10
if e > f:
    print("e大于f")

# 4. 小于 <
g = 5
h = 8
if g < h:
    print("g小于h")

# 5. 大于等于 >=
i = 10
j = 10
if i >= j:
    print("i大于等于j")

# 6. 小于等于 <=
k = 8
l = 10
if k <= l:
    print("k小于等于l")

# 示例：判断成绩
score = 75
if score == 100:
    print("满分！")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 示例：判断温度
temperature = 25
if temperature < 0:
    print("非常冷")
elif temperature < 15:
    print("比较冷")
elif temperature < 25:
    print("舒适")
else:
    print("比较热")

# 示例：比较字符串
password = "123456"
if password == "123456":
    print("密码正确")
else:
    print("密码错误")
