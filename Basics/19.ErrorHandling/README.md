# 错误处理教程.md

# Python 错误处理教程 

## 1. 什么是错误处理？

使用try-except捕获和处理错误。

## 2. 基本用法

```python
try:
    number = int(input("请输入数字: "))
except ValueError:
    print("输入的不是有效数字！")
```

## 3. 多个异常

```python
try:
    result = a / b
except ZeroDivisionError:
    print("不能除以零！")
```

## 4. else和finally

```python
try:
    # 尝试执行的代码
except:
    # 错误处理
else:
    # 没有错误时执行
finally:
    # 无论如何都执行
```

## 5. 总结

错误处理让程序更健壮！