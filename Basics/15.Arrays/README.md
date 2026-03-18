# 数组教程.md

# Python 数组教程 

## 1. 什么是数组？

数组是存储多个相同类型数据的容器。

## 2. Python中的数组

### 使用列表
```python
numbers = [1, 2, 3, 4, 5]
```

### 使用array模块
```python
import array
int_array = array.array('i', [1, 2, 3, 4, 5])
```

### 使用numpy（推荐）
```python
import numpy as np
np_array = np.array([1, 2, 3, 4, 5])
```

## 3. 常用操作

```python
numbers.append(6)   # 添加
numbers.remove(3)   # 删除
numbers[0] = 10     # 修改
```

## 4. 总结

Python通常用列表代替数组！