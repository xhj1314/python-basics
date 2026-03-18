# 日期教程.md

# Python 日期教程 

## 1. 什么是日期？

Python使用datetime模块处理日期和时间。

## 2. 获取当前时间

```python
from datetime import datetime

now = datetime.now()
print(now)
```

## 3. 格式化日期

```python
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
```

## 4. 日期计算

```python
from datetime import timedelta

tomorrow = today + timedelta(days=1)
```

## 5. 总结

datetime模块处理日期和时间！