# Python 字典教程 

## 1. 什么是字典？

字典是一个存储"键-值"对的容器，就像一本真正的字典，每个词（键）对应一个解释（值）。

### 生活中的类比
想象你有一本通讯录：
- 名字（键）对应电话号码（值）
- "张三" → "13800138000"
- "李四" → "13900139000"

字典就是这个"通讯录"，键就是"名字"，值就是"电话号码"。

### 创建字典
```python
student = {
    "name": "小明",    # "name"是键，"小明"是值
    "age": 18,         # "age"是键，18是值
    "city": "北京"     # "city"是键，"北京"是值
}

print("学生信息:", student)
```

## 2. 字典的特点

1. **用花括号 {} 创建**
2. **每个元素由"键:值"组成**
3. **键必须是唯一的**
4. **键必须是不可变的**（如字符串、数字、元组）
5. **值可以是任意类型**

## 3. 访问字典元素

### 通过键访问值
```python
student = {"name": "小明", "age": 18, "city": "北京"}

# 方法1：使用[]
print("姓名:", student["name"])  # 输出: 小明

# 方法2：使用get()（推荐）
print("姓名:", student.get("name"))  # 输出: 小明
print("性别:", student.get("gender", "未知"))  # 输出: 未知
```

### 获取所有键、值、键值对
```python
student = {"name": "小明", "age": 18, "city": "北京"}

# 获取所有键
keys = student.keys()
print("所有键:", list(keys))  # ['name', 'age', 'city']

# 获取所有值
values = student.values()
print("所有值:", list(values))  # ['小明', 18, '北京']

# 获取所有键值对
items = student.items()
print("所有键值对:", list(items))  # [('name', '小明'), ('age', 18), ('city', '北京')]
```

## 4. 修改字典

### 修改值
```python
student = {"name": "小明", "age": 18}
student["age"] = 19  # 修改年龄
print(student)  # {'name': '小明', 'age': 19}
```

### 添加新的键值对
```python
student = {"name": "小明", "age": 18}
student["city"] = "北京"  # 添加城市
print(student)  # {'name': '小明', 'age': 18, 'city': '北京'}
```

### 删除键值对
```python
student = {"name": "小明", "age": 18, "city": "北京"}

# 方法1：使用del
del student["city"]
print(student)  # {'name': '小明', 'age': 18}

# 方法2：使用pop()
age = student.pop("age")
print("删除的年龄:", age)  # 18
print(student)  # {'name': '小明'}
```

### 清空字典
```python
student = {"name": "小明", "age": 18}
student.clear()
print(student)  # {}
```

### 批量更新
```python
student = {"name": "小明", "age": 18}
student.update({"city": "北京", "gender": "男"})
print(student)  # {'name': '小明', 'age': 18, 'city': '北京', 'gender': '男'}
```

## 5. 遍历字典

### 遍历所有键
```python
student = {"name": "小明", "age": 18, "city": "北京"}

for key in student:
    print("键:", key)
```

### 遍历所有值
```python
student = {"name": "小明", "age": 18, "city": "北京"}

for value in student.values():
    print("值:", value)
```

### 遍历所有键值对（推荐）
```python
student = {"name": "小明", "age": 18, "city": "北京"}

for key, value in student.items():
    print(f"{key}: {value}")
```

## 6. 实践练习

### 练习1：通讯录
```python
# 创建通讯录
contacts = {
    "张三": "13800138000",
    "李四": "13900139000",
    "王五": "13700137000"
}

# 查找电话
name = "张三"
if name in contacts:
    print(f"{name}的电话: {contacts[name]}")
else:
    print(f"没有找到{name}的电话")

# 添加新联系人
contacts["赵六"] = "13600136000"
print("通讯录:", contacts)
```

### 练习2：商品价格
```python
# 创建价格表
prices = {
    "苹果": 5.5,
    "香蕉": 3.2,
    "橙子": 4.8
}

# 计算总价
shopping_list = ["苹果", "香蕉", "橙子", "苹果"]
total = 0

for item in shopping_list:
    if item in prices:
        total += prices[item]
        print(f"{item}: {prices[item]}元")

print(f"总价: {total}元")
```

### 练习3：单词计数
```python
# 统计单词出现次数
text = "apple banana apple orange banana apple"
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("单词计数:", word_count)
# 输出: {'apple': 3, 'banana': 2, 'orange': 1}
```

## 7. 常见问题解答

### Q1: 字典和列表有什么区别？
**A:**
- 列表用索引（数字）访问元素
- 字典用键（任意不可变类型）访问元素
- 列表有序，字典在Python 3.7+有序

### Q2: 什么时候用字典？
**A:** 当需要通过"名字"而不是"位置"来访问数据时，用字典。例如：
- 通讯录（名字→电话）
- 配置信息（配置项→值）
- 学生信息（属性→值）

### Q3: 键可以是什么类型？
**A:** 键必须是不可变类型：
- 可以：字符串、数字、元组
- 不可以：列表、字典

### Q4: 如何检查键是否存在？
**A:** 使用 `in` 关键字：
```python
student = {"name": "小明", "age": 18}
if "name" in student:
    print("name键存在")
```

## 8. 总结

字典是Python中非常重要的数据结构，掌握字典的使用非常重要。

### 核心要点
1. **字典存储键值对**
2. **通过键访问值**
3. **键必须是唯一的和不可变的**
4. **可以添加、修改、删除键值对**
5. **可以遍历字典的键、值、键值对**

### 学习建议
1. 多练习创建和使用字典
2. 理解键值对的概念
3. 掌握字典的常用方法
4. 尝试解决实际问题

通过本教程，你应该已经掌握了字典的基本使用方法。继续练习，你会发现字典在Python编程中无处不在！