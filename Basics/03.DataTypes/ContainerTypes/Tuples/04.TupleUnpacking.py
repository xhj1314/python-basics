# 元组解包

# 什么是元组解包？
# 将元组中的元素一次性赋值给多个变量

# 基本解包
person = ("小明", 18, "北京")
name, age, city = person
print("姓名:", name)
print("年龄:", age)
print("城市:", city)

# 交换变量
a = 10
b = 20
print(f"\n交换前: a={a}, b={b}")
a, b = b, a  # 使用元组解包交换
print(f"交换后: a={a}, b={b}")

# 使用*收集多余元素
scores = (90, 85, 92, 78, 88)
first, *middle, last = scores
print("\n第一个分数:", first)
print("中间分数:", middle)
print("最后一个分数:", last)

# 函数返回多个值
def get_info():
    return "小红", 20, "上海"

name, age, city = get_info()
print(f"\n函数返回: 姓名={name}, 年龄={age}, 城市={city}")
