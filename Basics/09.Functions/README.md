# 函数教程.md

# Python 函数教程 

## 1. 什么是函数？

函数是一段可重复使用的代码块，用于完成特定任务。

## 2. 定义函数

```python
def 函数名(参数):
    函数体
    return 返回值
```

## 3. 参数类型

### 位置参数
```python
def add(a, b):
    return a + b

add(3, 5)  # 8
```

### 默认参数
```python
def greet(name, title="先生"):
    print(f"{title} {name}")

greet("张三")  # 先生 张三
```

### 可变参数
```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # 15
```

## 4. 返回值

```python
# 单个返回值
def square(x):
    return x ** 2

# 多个返回值
def get_min_max(numbers):
    return min(numbers), max(numbers)
```

## 5. 实践练习

```python
# 计算BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.2f}")
```

## 6. 总结

函数让代码更简洁、可重用！