# 字符串操作

# 创建字符串
str1 = "Hello"
str2 = "World"

# 1. 字符串拼接
result = str1 + " " + str2
print("拼接:", result)  # Hello World

# 2. 字符串重复
repeat = "哈" * 3
print("重复:", repeat)  # 哈哈哈

# 3. 字符串长度
text = "Python"
print("长度:", len(text))  # 6

# 4. 大小写转换
text = "Hello World"
print("\n大小写转换:")
print("大写:", text.upper())      # HELLO WORLD
print("小写:", text.lower())      # hello world
print("首字母大写:", text.capitalize())  # Hello world
print("每个单词首字母大写:", text.title())  # Hello World

# 5. 去除空格
text = "  Hello World  "
print("\n去除空格:")
print("去除两端空格:", text.strip())   # "Hello World"
print("去除左边空格:", text.lstrip())  # "Hello World  "
print("去除右边空格:", text.rstrip())  # "  Hello World"

# 6. 查找和替换
text = "Hello World"
print("\n查找和替换:")
print("查找World的位置:", text.find("World"))  # 6
print("替换World:", text.replace("World", "Python"))  # Hello Python

# 7. 分割和连接
text = "苹果,香蕉,橙子"
fruits = text.split(",")
print("\n分割:", fruits)  # ['苹果', '香蕉', '橙子']

result = "-".join(fruits)
print("连接:", result)  # 苹果-香蕉-橙子
