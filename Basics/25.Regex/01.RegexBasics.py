# 正则表达式基础

# 什么是正则表达式？
# 正则表达式是用于匹配字符串模式的工具

import re

# 1. 匹配
pattern = r"hello"
text = "hello world"
match = re.match(pattern, text)
if match:
    print(f"匹配成功: {match.group()}")
print("\n")

# 2. 搜索
text = "say hello to the world"
search = re.search(pattern, text)
if search:
    print(f"找到: {search.group()}")
print("\n")

# 3. 查找所有
text = "hello world, hello python"
matches = re.findall(pattern, text)
print(f"所有匹配: {matches}")
print("\n")

# 4. 替换
text = "hello world"
new_text = re.sub(pattern, "hi", text)
print(f"替换后: {new_text}")
print("\n")

# 5. 分割
text = "apple,banana,orange"
parts = re.split(r",", text)
print(f"分割: {parts}")

# 6. 常用模式
# \d - 数字
# \w - 字母数字下划线
# \s - 空白字符
# . - 任意字符
# * - 0次或多次
# + - 1次或多次
# ? - 0次或1次
