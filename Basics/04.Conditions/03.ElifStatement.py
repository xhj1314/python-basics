# elif语句

# 什么是elif语句？
# elif是"else if"的缩写，用于检查多个条件

# 基本语法：
# if 条件1:
#     条件1成立时执行
# elif 条件2:
#     条件2成立时执行
# else:
#     所有条件都不成立时执行

# 示例1：成绩等级判断
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 示例2：判断年龄段
age = 25
if age < 13:
    print("儿童")
elif age < 18:
    print("青少年")
elif age < 60:
    print("成年人")
else:
    print("老年人")

# 示例3：比较三个数字
a = 10
b = 20
c = 30
if a > b and a > c:
    print("a最大")
elif b > a and b > c:
    print("b最大")
else:
    print("c最大")

# 示例4：判断季节
month = 7
if month in [3, 4, 5]:
    print("春天")
elif month in [6, 7, 8]:
    print("夏天")
elif month in [9, 10, 11]:
    print("秋天")
else:
    print("冬天")
