# 迭代教程.md

# Python 迭代教程 

## 1. 什么是迭代？

迭代是遍历序列中每个元素的过程。

## 2. 可迭代对象

```python
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)
```

## 3. 迭代器

```python
iterator = iter(fruits)
print(next(iterator))  # 苹果
```

## 4. 生成器

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
```

## 5. 总结

迭代让遍历更简单！