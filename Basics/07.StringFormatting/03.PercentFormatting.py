# %格式化

# 什么是%格式化？
# %格式化是Python早期的字符串格式化方法

# 基本语法："文本%s文本" % 值

# 示例1：字符串
name = "小明"
print("姓名: %s" % name)
print("\n")

# 示例2：整数
age = 18
print("年龄: %d岁" % age)
print("\n")

# 示例3：浮点数
price = 19.99
print("价格: %.2f元" % price)
print("\n")

# 示例4：多个值
print("姓名: %s, 年龄: %d" % (name, age))
print("\n")

# 示例5：百分比
score = 85
print("得分率: %.1f%%" % score)

# 常用格式化符号：
# %s - 字符串
# %d - 整数
# %f - 浮点数
# %.nf - 保留n位小数
# %% - 百分号

# 注意：推荐使用f-string或format方法，%格式化是旧方法
