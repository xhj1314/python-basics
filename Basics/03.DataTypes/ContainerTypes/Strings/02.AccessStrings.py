# 访问字符串

# 创建字符串
text = "Hello, Python!"

# 通过索引访问字符（从0开始）
print("第一个字符:", text[0])    # H
print("第二个字符:", text[1])    # e
print("最后一个字符:", text[-1])  # !

# 切片访问
print("\n切片访问:")
print("前5个字符:", text[:5])      # Hello
print("第7个开始:", text[7:])      # Python!
print("中间部分:", text[7:13])     # Python

# 遍历字符串
print("\n遍历字符串:")
for char in text:
    print("字符:", char)

# 带索引遍历
print("\n带索引遍历:")
for index, char in enumerate(text):
    print(f"{index}: {char}")

# 获取字符串长度
length = len(text)
print("\n字符串长度:", length)
