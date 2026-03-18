# None教程.md

# Python None教程 

## 1. 什么是None？

None表示"无"或"空"。

## 2. 检查None

```python
x = None
if x is None:
    print("x是None")
```

## 3. 函数返回None

```python
def my_function():
    pass  # 默认返回None
```

## 4. None作为默认值

```python
def greet(name=None):
    if name is None:
        name = "陌生人"
    print(f"你好, {name}!")
```

## 5. 总结

None表示"无"！