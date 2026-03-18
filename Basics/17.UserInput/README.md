# 用户输入教程.md

# Python 用户输入教程 

## 1. 什么是用户输入？

使用input()函数获取用户输入。

## 2. 基本用法

```python
name = input("请输入你的名字: ")
print(f"你好, {name}!")
```

## 3. 输入数字

```python
age = int(input("请输入年龄: "))  # 整数
height = float(input("请输入身高: "))  # 浮点数
```

## 4. 输入验证

```python
while True:
    password = input("请输入密码: ")
    if password == "123456":
        print("正确！")
        break
```

## 5. 总结

input()返回字符串，需要转换类型！