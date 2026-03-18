# lambda教程.md

# Python lambda教程 

## 1. 什么是lambda？

lambda是匿名函数，用于创建简单的单行函数。

## 2. 基本语法

```python
lambda 参数: 表达式
```

## 3. 示例

```python
# 平方函数
square = lambda x: x ** 2
print(square(5))  # 25

# 加法函数
add = lambda a, b: a + b
print(add(3, 5))  # 8
```

## 4. 常用场景

### 与map配合
```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
```

### 与filter配合
```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

## 5. 总结

lambda适合简单的单行函数！