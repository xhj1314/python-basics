# 集合教程.md

# Python 集合教程 

## 1. 什么是集合？

集合是一个无序的、不重复的元素集合。

## 2. 创建集合

```python
fruits = {"苹果", "香蕉", "橙子"}
empty_set = set()  # 空集合
```

## 3. 常用操作

```python
# 添加
fruits.add("葡萄")

# 删除
fruits.remove("香蕉")

# 去重
numbers = [1, 2, 2, 3, 3, 4]
unique = set(numbers)  # {1, 2, 3, 4}
```

## 4. 集合运算

```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b  # 并集 {1, 2, 3, 4}
a & b  # 交集 {2, 3}
a - b  # 差集 {1}
```

## 5. 总结

集合适合去重和集合运算！