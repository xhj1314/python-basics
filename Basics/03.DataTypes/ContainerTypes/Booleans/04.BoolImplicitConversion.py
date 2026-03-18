# 布尔值的隐式转换

# Python 中几乎所有值都可以被隐式转换为 bool 值

# False 等价的值（假值）：
# None, False, 0, ""（空字符串）, []（空列表）, {}（空字典）, ()（空元组）

# True 等价的值（真值）：
# 其他所有非空、非零的值

# 隐式转换示例
print("bool(0) =", bool(0))      # False
print("bool(10) =", bool(10))     # True
print("bool('') =", bool(""))     # False
print("bool('Hi') =", bool("Hi"))   # True
print("bool([]) =", bool([]))     # False
print("bool([1, 2]) =", bool([1, 2])) # True
print("bool(None) =", bool(None))   # False
print("bool({}) =", bool({}))     # False
print("bool(()) =", bool(()))     # False

# 应用场景
# 条件判断：if、while 等语句会自动转换条件为 bool 值

# 示例1：检查字符串是否为空
name = ""
if name:  # 等价于 if bool(name) → False
    print("Hello, " + name)
else:
    print("Name is empty!")  # 会执行这里

# 示例2：检查列表是否为空
items = []
if items:
    print("列表有元素")
else:
    print("列表为空")  # 会执行这里

# 示例3：检查数字是否为零
count = 0
if count:
    print("count 不为零")
else:
    print("count 为零")  # 会执行这里