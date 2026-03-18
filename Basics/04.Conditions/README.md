# 条件语句教程.md

# Python 条件语句教程 

## 1. 什么是条件语句？

条件语句用于根据条件决定执行哪些代码。就像生活中的选择：
- 如果下雨，就带伞
- 如果成绩及格，就通过
- 如果是周末，就休息

## 2. if语句

### 基本语法
```python
if 条件:
    执行的代码
```

### 示例
```python
age = 18
if age >= 18:
    print("你已经成年了")
```

### 注意事项
1. 条件后面要加冒号`:`
2. 执行的代码要缩进（4个空格）
3. 条件必须是布尔值（True或False）

## 3. if-else语句

### 基本语法
```python
if 条件:
    条件成立时执行
else:
    条件不成立时执行
```

### 示例
```python
age = 15
if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")
```

## 4. if-elif-else语句

### 基本语法
```python
if 条件1:
    条件1成立时执行
elif 条件2:
    条件2成立时执行
else:
    所有条件都不成立时执行
```

### 示例
```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

## 5. 比较运算符

| 运算符 | 说明 | 示例 |
|--------|------|------|
| == | 等于 | a == b |
| != | 不等于 | a != b |
| > | 大于 | a > b |
| < | 小于 | a < b |
| >= | 大于等于 | a >= b |
| <= | 小于等于 | a <= b |

## 6. 逻辑运算符

| 运算符 | 说明 | 示例 |
|--------|------|------|
| and | 与（两个都成立） | a > 0 and b > 0 |
| or | 或（任意一个成立） | a > 0 or b > 0 |
| not | 非（取反） | not a > 0 |

### 示例
```python
# and - 两个条件都成立
age = 20
has_id = True
if age >= 18 and has_id:
    print("可以进入网吧")

# or - 任意一个条件成立
score = 85
is_vip = True
if score >= 90 or is_vip:
    print("可以获得奖励")

# not - 取反
is_raining = False
if not is_raining:
    print("可以出去玩")
```

## 7. 嵌套if语句

在if语句内部再使用if语句：

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("可以看电影")
    else:
        print("需要买票")
else:
    print("年龄不够，不能看")
```

## 8. 三元表达式

三元表达式是if-else的简写形式：

### 基本语法
```python
值1 if 条件 else 值2
```

### 示例
```python
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)  # 输出: 成年

# 判断奇偶数
number = 7
result = "偶数" if number % 2 == 0 else "奇数"
print(result)  # 输出: 奇数
```

## 9. 实践练习

### 练习1：判断成绩等级
```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

### 练习2：判断闰年
```python
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")
```

### 练习3：计算BMI并判断体型
```python
height = 1.75  # 米
weight = 70    # 公斤
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"BMI: {bmi:.1f} - 偏瘦")
elif bmi < 24:
    print(f"BMI: {bmi:.1f} - 正常")
elif bmi < 28:
    print(f"BMI: {bmi:.1f} - 偏胖")
else:
    print(f"BMI: {bmi:.1f} - 肥胖")
```

## 10. 常见问题解答

### Q1: if和elif的区别？
**A:** if是第一个条件，elif是后续条件。程序会从上到下检查，遇到第一个成立的条件就执行。

### Q2: else必须写吗？
**A:** 不必须。如果不需要处理其他情况，可以不写else。

### Q3: 可以有多少个elif？
**A:** 可以有任意多个elif，但建议不要太多，影响可读性。

### Q4: 缩进必须用4个空格吗？
**A:** 建议用4个空格，这是Python的标准。也可以用Tab，但要保持一致。

## 11. 总结

条件语句是Python编程的基础，掌握条件语句非常重要。

### 核心要点
1. **if语句用于判断条件**
2. **else处理其他情况**
3. **elif检查多个条件**
4. **比较运算符用于比较值**
5. **逻辑运算符用于组合条件**

### 学习建议
1. 多练习各种条件判断
2. 理解条件的执行顺序
3. 注意缩进和冒号
4. 尝试解决实际问题

通过本教程，你应该已经掌握了条件语句的基本使用方法。继续练习，你会发现条件语句在Python编程中无处不在！