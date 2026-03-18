# 字符串教程.md

# Python 字符串教程 

## 1. 什么是字符串？

字符串是用引号包围的文本，用于存储文字信息。

### 生活中的类比
想象你在写一封信：
- 信的内容就是字符串
- 每个字就是一个字符
- 整封信就是一个字符串

### 创建字符串
```python
name = "小明"           # 双引号
message = '你好世界'     # 单引号
long_text = """这是
多行
字符串"""              # 三引号

print("姓名:", name)
print("消息:", message)
```

## 2. 字符串的特点

1. **用引号包围**（单引号、双引号、三引号）
2. **不可变**（创建后不能修改）
3. **有序**（可以通过索引访问）
4. **可以包含任何字符**

### 转义字符
```python
print("换行: 第一行\n第二行")      # \n 换行
print("制表符: 名字\t年龄")        # \t 制表符
print("引号: 他说\"你好\"")        # \" 引号
```

### 原始字符串
```python
# 不转义，原样输出
raw_string = r"C:\Users\name\folder"
print(raw_string)  # C:\Users\name\folder
```

## 3. 访问字符串

### 通过索引访问
```python
text = "Hello, Python!"

print("第一个字符:", text[0])    # H
print("第二个字符:", text[1])    # e
print("最后一个字符:", text[-1])  # !
```

### 切片访问
```python
text = "Hello, Python!"

print("前5个字符:", text[:5])      # Hello
print("第7个开始:", text[7:])      # Python!
print("中间部分:", text[7:13])     # Python
```

### 遍历字符串
```python
text = "Hello"

for char in text:
    print("字符:", char)
```

## 4. 字符串操作

### 拼接字符串
```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Hello World
```

### 重复字符串
```python
repeat = "哈" * 3
print(repeat)  # 哈哈哈
```

### 大小写转换
```python
text = "Hello World"

print("大写:", text.upper())        # HELLO WORLD
print("小写:", text.lower())        # hello world
print("首字母大写:", text.capitalize())  # Hello world
print("每个单词首字母大写:", text.title())  # Hello World
```

### 去除空格
```python
text = "  Hello World  "

print("去除两端空格:", text.strip())   # "Hello World"
print("去除左边空格:", text.lstrip())  # "Hello World  "
print("去除右边空格:", text.rstrip())  # "  Hello World"
```

### 查找和替换
```python
text = "Hello World"

print("查找World的位置:", text.find("World"))  # 6
print("替换World:", text.replace("World", "Python"))  # Hello Python
```

### 分割和连接
```python
# 分割
text = "苹果,香蕉,橙子"
fruits = text.split(",")
print(fruits)  # ['苹果', '香蕉', '橙子']

# 连接
result = "-".join(fruits)
print(result)  # 苹果-香蕉-橙子
```

## 5. 字符串格式化

### 使用f-string（推荐）
```python
name = "小明"
age = 18
print(f"姓名: {name}, 年龄: {age}")
```

### 使用format()方法
```python
name = "小明"
age = 18
print("姓名: {}, 年龄: {}".format(name, age))
```

### 格式化数字
```python
price = 19.99
quantity = 5
total = price * quantity

print(f"商品价格: {price:.2f}元")
print(f"购买数量: {quantity}个")
print(f"总价: {total:.2f}元")
```

## 6. 常用字符串方法

### 检查开头和结尾
```python
text = "Hello World"
print(text.startswith("Hello"))  # True
print(text.endswith("World"))    # True
```

### 检查包含
```python
text = "Hello World"
print("World" in text)        # True
print(text.find("World"))     # 6
```

### 统计出现次数
```python
text = "Hello Hello Hello"
print(text.count("Hello"))  # 3
```

### 判断类型
```python
print("123".isdigit())      # True - 是否全是数字
print("abc".isalpha())      # True - 是否全是字母
print("abc123".isalnum())   # True - 是否全是字母或数字
print("   ".isspace())      # True - 是否全是空格
```

### 填充和对齐
```python
text = "Python"
print(text.ljust(10, "-"))   # Python----
print(text.rjust(10, "-"))   # ----Python
print(text.center(10, "-"))  # --Python--
```

## 7. 实践练习

### 练习1：用户信息
```python
# 创建用户信息字符串
name = "张三"
age = 25
city = "北京"

# 使用格式化输出
print(f"用户信息:")
print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"城市: {city}")
```

### 练习2：邮箱验证
```python
email = "user@example.com"

# 检查是否包含@
if "@" in email:
    print("邮箱格式正确")
    # 分割用户名和域名
    username, domain = email.split("@")
    print(f"用户名: {username}")
    print(f"域名: {domain}")
else:
    print("邮箱格式错误")
```

### 练习3：文本处理
```python
# 处理用户输入
user_input = "  Hello, World!  "

# 去除空格
cleaned = user_input.strip()
print(f"清理后: '{cleaned}'")

# 转小写
lower_text = cleaned.lower()
print(f"小写: '{lower_text}'")

# 替换
replaced = cleaned.replace("World", "Python")
print(f"替换后: '{replaced}'")
```

## 8. 常见问题解答

### Q1: 字符串可以修改吗？
**A:** 不能！字符串是不可变的。
```python
text = "Hello"
# text[0] = "h"  # 错误！不能修改

# 只能创建新字符串
new_text = "h" + text[1:]
print(new_text)  # hello
```

### Q2: 单引号和双引号有什么区别？
**A:** 没有区别，可以互换使用。但要注意：
```python
# 如果字符串包含单引号，用双引号
text1 = "It's a book"

# 如果字符串包含双引号，用单引号
text2 = '他说"你好"'
```

### Q3: 如何判断字符串是否为空？
**A:** 使用 `len()` 或直接判断：
```python
text = ""
if len(text) == 0:
    print("字符串为空")

# 或者
if not text:
    print("字符串为空")
```

### Q4: 如何反转字符串？
**A:** 使用切片：
```python
text = "Hello"
reversed_text = text[::-1]
print(reversed_text)  # olleH
```

## 9. 总结

字符串是Python中最常用的数据类型之一，掌握字符串的使用非常重要。

### 核心要点
1. **字符串用引号包围**
2. **字符串是不可变的**
3. **可以通过索引和切片访问**
4. **支持各种操作和方法**
5. **格式化可以插入变量值**

### 学习建议
1. 多练习字符串的基本操作
2. 掌握常用的字符串方法
3. 学会使用字符串格式化
4. 尝试解决实际问题

通过本教程，你应该已经掌握了字符串的基本使用方法。继续练习，你会发现字符串在Python编程中无处不在！