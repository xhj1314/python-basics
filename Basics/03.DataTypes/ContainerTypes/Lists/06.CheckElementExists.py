# 检查列表元素是否存在

# 使用 in 关键字检查元素是否在列表中

# 创建一个列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("水果列表:", fruits)

# 检查元素是否存在
if "苹果" in fruits:
    print("苹果在列表中！")  # 会执行这行

if "西瓜" in fruits:
    print("西瓜在列表中！")
else:
    print("西瓜不在列表中！")  # 会执行这行

# 使用 not in 检查元素是否不存在
if "西瓜" not in fruits:
    print("西瓜不在列表中，需要添加！")  # 会执行这行

# 查找元素的索引
index = fruits.index("香蕉")
print("香蕉的索引是:", index)  # 输出: 1

# 注意：如果元素不存在，index()会报错
# fruits.index("西瓜")  # 错误！ValueError: '西瓜' is not in list

# 安全的查找方法
if "西瓜" in fruits:
    index = fruits.index("西瓜")
    print("西瓜的索引是:", index)
else:
    print("西瓜不在列表中")

# 统计元素出现的次数
numbers = [1, 2, 3, 2, 4, 2, 5]
print("\n数字列表:", numbers)
print("数字2出现的次数:", numbers.count(2))  # 输出: 3
print("数字5出现的次数:", numbers.count(5))  # 输出: 1
print("数字10出现的次数:", numbers.count(10))  # 输出: 0

# 总结：
# in - 检查元素是否在列表中，返回True或False
# not in - 检查元素是否不在列表中，返回True或False
# index(值) - 返回元素的索引，如果不存在会报错
# count(值) - 返回元素出现的次数
