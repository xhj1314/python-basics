# 元组操作

# 创建元组
fruits = ("苹果", "香蕉", "橙子")

# 1. 连接元组
more_fruits = ("葡萄", "西瓜")
all_fruits = fruits + more_fruits
print("连接后的元组:", all_fruits)

# 2. 重复元组
repeat = ("哈",) * 3
print("重复元组:", repeat)  # ('哈', '哈', '哈')

# 3. 检查元素是否存在
print("\n检查元素是否存在:")
if "苹果" in fruits:
    print("苹果在元组中")
else:
    print("苹果不在元组中")

# 4. 获取元素数量
count = len(fruits)
print("\n元素数量:", count)

# 5. 统计元素出现次数
numbers = (1, 2, 3, 2, 2, 4)
two_count = numbers.count(2)
print("2出现的次数:", two_count)

# 6. 查找元素索引
index = fruits.index("香蕉")
print("香蕉的索引:", index)
