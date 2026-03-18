# while循环教程.md

# Python while循环教程 

## 1. 什么是while循环？

while循环在条件为True时重复执行代码块，直到条件变为False。

### 生活中的类比
想象你在排队买票：
- 当前面还有人时，继续等待
- 当前面没人时，停止等待，去买票

## 2. 基本语法

```python
while 条件:
    执行的代码
```

## 3. 基本示例

```python
# 倒计时
count = 5
while count > 0:
    print(count)
    count -= 1
print("发射！")
```

## 4. 循环控制

### break - 跳出循环
```python
while True:
    password = input("请输入密码: ")
    if password == "123456":
        print("密码正确！")
        break
```

### continue - 跳过本次
```python
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # 跳过偶数
    print(num)  # 只打印奇数
```

### else - 循环结束后执行
```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("循环结束")
```

## 5. 无限循环

条件永远为True的循环：

```python
while True:
    # 执行代码
    if 退出条件:
        break
```

## 6. for vs while

| 特性 | for循环 | while循环 |
|------|---------|-----------|
| 用途 | 遍历序列 | 条件循环 |
| 循环次数 | 已知 | 可能未知 |
| 适用场景 | 列表、字符串等 | 用户输入、游戏等 |

## 7. 实践练习

### 练习1：计算阶乘
```python
n = 5
result = 1
while n > 0:
    result *= n
    n -= 1
print(f"5的阶乘: {result}")  # 120
```

### 练习2：猜数字游戏
```python
import random
target = random.randint(1, 100)
while True:
    guess = int(input("猜数字(1-100): "))
    if guess == target:
        print("正确！")
        break
    elif guess < target:
        print("太小")
    else:
        print("太大")
```

### 练习3：斐波那契数列
```python
a, b = 0, 1
count = 0
while count < 10:
    print(a)
    a, b = b, a + b
    count += 1
```

## 8. 常见问题解答

### Q1: while和for的区别？
**A:**
- while适合不确定循环次数的情况
- for适合遍历已知序列

### Q2: 如何避免无限循环？
**A:** 确保条件最终会变为False，或在循环内使用break。

### Q3: break和continue的区别？
**A:**
- break：跳出整个循环
- continue：跳过本次，继续下一次

## 9. 总结

while循环是Python中重要的循环结构。

### 核心要点
1. **条件为True时执行**
2. **条件最终要变为False**
3. **break跳出，continue跳过**
4. **无限循环需要退出条件**

### 学习建议
1. 理解循环条件的设置
2. 注意避免无限循环
3. 掌握循环控制语句
4. 尝试解决实际问题

通过本教程，你应该已经掌握了while循环的基本使用方法！