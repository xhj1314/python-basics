# 访问元组元素

# 创建元组
fruits = ("苹果", "香蕉", "橙子", "葡萄", "西瓜")

# 通过索引访问（从0开始）
print("第一个:", fruits[0])    # 苹果
print("第二个:", fruits[1])    # 香蕉
print("最后一个:", fruits[-1])  # 西瓜

# 切片访问
print("\n切片访问:")
print("前两个:", fruits[:2])     # ('苹果', '香蕉')
print("后两个:", fruits[-2:])    # ('葡萄', '西瓜')
print("中间三个:", fruits[1:4])  # ('香蕉', '橙子', '葡萄')

# 遍历元组
print("\n遍历元组:")
for fruit in fruits:
    print("水果:", fruit)

# 带索引遍历
print("\n带索引遍历:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")
