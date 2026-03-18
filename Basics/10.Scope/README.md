# 作用域教程.md

# Python 作用域教程 

## 1. 什么是作用域？

作用域是变量的有效范围。

## 2. 局部变量

在函数内部定义的变量，只能在函数内使用：

```python
def my_function():
    local_var = 10  # 局部变量
    print(local_var)

my_function()
# print(local_var)  # 错误！
```

## 3. 全局变量

在函数外部定义的变量，可以在任何地方使用：

```python
global_var = 100  # 全局变量

def my_function():
    print(global_var)

my_function()
```

## 4. 修改全局变量

使用global关键字：

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1
```

## 5. 总结

- 局部变量：函数内定义，函数内使用
- 全局变量：函数外定义，任何地方使用
- global：在函数内修改全局变量