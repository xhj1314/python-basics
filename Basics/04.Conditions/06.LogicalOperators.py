# 逻辑运算符

# 什么是逻辑运算符？
# 用于组合多个条件

# 1. and运算符（与）- 两个条件都成立才为True
age = 20
has_id = True

if age >= 18 and has_id:
    print("可以进入网吧")
else:
    print("不能进入网吧")

# 2. or运算符（或）- 任意一个条件成立就为True
score = 85
is_vip = True

if score >= 90 or is_vip:
    print("可以获得奖励")
else:
    print("不能获得奖励")

# 3. not运算符（非）- 取反
is_raining = False

if not is_raining:
    print("可以出去玩")
else:
    print("在家待着")

# 示例：综合使用
age = 25
has_license = True
has_car = False

# and和or组合使用
if age >= 18 and has_license:
    if has_car:
        print("可以开车")
    else:
        print("可以租车开")
else:
    print("不能开车")

# 示例：判断闰年
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")

# 示例：判断三角形类型
a, b, c = 3, 4, 5
if a == b == c:
    print("等边三角形")
elif a == b or b == c or a == c:
    print("等腰三角形")
else:
    print("普通三角形")
