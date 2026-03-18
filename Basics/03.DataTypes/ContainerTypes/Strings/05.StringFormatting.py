# 字符串格式化

# 什么是字符串格式化？
# 将变量的值插入到字符串中

# 方法1：使用f-string（推荐，Python 3.6+）
name = "小明"
age = 18
print(f"姓名: {name}, 年龄: {age}")

# 方法2：使用format()方法
print("姓名: {}, 年龄: {}".format(name, age))
print("姓名: {0}, 年龄: {1}".format(name, age))
print("姓名: {name}, 年龄: {age}".format(name=name, age=age))

# 方法3：使用%格式化（旧方法）
print("姓名: %s, 年龄: %d" % (name, age))

# 格式化数字
price = 19.99
quantity = 5
total = price * quantity

print(f"\n商品价格: {price:.2f}元")
print(f"购买数量: {quantity}个")
print(f"总价: {total:.2f}元")

# 格式化对齐
print("\n对齐格式化:")
print(f"{'商品':<10}{'价格':>10}")  # 左对齐和右对齐
print(f"{'苹果':<10}{5.5:>10.2f}")
print(f"{'香蕉':<10}{3.2:>10.2f}")

# 格式化百分比
score = 85
total_score = 100
percentage = score / total_score * 100
print(f"\n得分率: {percentage:.1f}%")
