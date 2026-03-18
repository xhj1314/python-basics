# 嵌套if语句

# 什么是嵌套if？
# 在一个if语句内部再使用if语句

# 示例1：判断是否可以看电影
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("可以看电影")
    else:
        print("需要买票")
else:
    print("年龄不够，不能看")

# 示例2：判断成绩等级（嵌套版）
score = 85
if score >= 60:
    print("及格了")
    if score >= 90:
        print("优秀！")
    elif score >= 80:
        print("良好！")
    else:
        print("继续努力！")
else:
    print("不及格")

# 示例3：判断登录状态
username = "admin"
password = "123456"
is_active = True

if username == "admin":
    if password == "123456":
        if is_active:
            print("登录成功")
        else:
            print("账号已被禁用")
    else:
        print("密码错误")
else:
    print("用户名不存在")

# 示例4：判断数字范围
number = 15
if number > 0:
    print("正数")
    if number < 10:
        print("小于10的正数")
    elif number < 20:
        print("10到20之间的正数")
    else:
        print("大于等于20的正数")
else:
    print("非正数")

# 注意：嵌套层次不要太深，否则代码难以阅读
