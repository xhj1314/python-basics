# 字符串方法

# 创建字符串
text = "  Hello, Python World!  "

# 1. 检查开头和结尾
print("检查开头和结尾:")
print("是否以Hello开头:", text.strip().startswith("Hello"))
print("是否以World结尾:", text.strip().endswith("World"))

# 2. 检查包含
print("\n检查包含:")
print("是否包含Python:", "Python" in text)
print("Python的位置:", text.find("Python"))

# 3. 统计和查找
print("\n统计和查找:")
sample = "Hello Hello Hello"
print("Hello出现次数:", sample.count("Hello"))

# 4. 判断类型
print("\n判断类型:")
print("'123'.isdigit():", "123".isdigit())      # 是否全是数字
print("'abc'.isalpha():", "abc".isalpha())      # 是否全是字母
print("'abc123'.isalnum():", "abc123".isalnum())  # 是否全是字母或数字
print("'   '.isspace():", "   ".isspace())      # 是否全是空格

# 5. 大小写判断
print("\n大小写判断:")
print("'HELLO'.isupper():", "HELLO".isupper())  # 是否全大写
print("'hello'.islower():", "hello".islower())  # 是否全小写
print("'Hello World'.istitle():", "Hello World".istitle())  # 是否标题格式

# 6. 填充和对齐
print("\n填充和对齐:")
text = "Python"
print("左对齐:", text.ljust(10, "-"))   # Python----
print("右对齐:", text.rjust(10, "-"))   # ----Python
print("居中:", text.center(10, "-"))    # --Python--

# 7. 去除字符
print("\n去除字符:")
text = "xxHelloxx"
print("去除两端x:", text.strip("x"))   # Hello
print("去除左边x:", text.lstrip("x"))  # Helloxx
print("去除右边x:", text.rstrip("x"))  # xxHello
