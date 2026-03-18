# 列表常用方法

# 创建一个列表
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("原始列表:", numbers)

# 1. 排序（从小到大）
numbers.sort()
print("sort排序后:", numbers)  # 输出: [1, 1, 2, 3, 4, 5, 6, 9]

# 2. 排序（从大到小）
numbers.sort(reverse=True)
print("sort降序排序后:", numbers)  # 输出: [9, 6, 5, 4, 3, 2, 1, 1]

# 3. 反转列表
numbers.reverse()
print("reverse反转后:", numbers)  # 输出: [1, 1, 2, 3, 4, 5, 6, 9]

# 4. 获取列表长度
length = len(numbers)
print("列表长度:", length)  # 输出: 8

# 5. 获取最大值和最小值
print("最大值:", max(numbers))  # 输出: 9
print("最小值:", min(numbers))  # 输出: 1

# 6. 计算列表元素的和
print("元素总和:", sum(numbers))  # 输出: 31

# 7. 复制列表
numbers_copy = numbers.copy()
print("复制的列表:", numbers_copy)

# 8. 清空列表
temp_list = [1, 2, 3]
print("\n临时列表:", temp_list)
temp_list.clear()
print("clear清空后:", temp_list)  # 输出: []

# 示例：字符串列表排序
fruits = ["香蕉", "苹果", "橙子", "葡萄"]
print("\n水果列表:", fruits)
fruits.sort()
print("排序后:", fruits)  # 输出: ['苹果', '橙子', '葡萄', '香蕉']（按拼音排序）

# 总结：
# sort() - 排序（默认从小到大）
# sort(reverse=True) - 降序排序
# reverse() - 反转列表
# len() - 获取长度
# max() - 获取最大值
# min() - 获取最小值
# sum() - 计算总和
# copy() - 复制列表
# clear() - 清空列表
