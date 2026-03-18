# 字符串格式化教程.md

# Python 字符串格式化教程 

## 1. 什么是字符串格式化？

字符串格式化是将变量的值插入到字符串中的方法。

## 2. f-string（推荐）

Python 3.6+推荐使用的方法：

```python
name = "小明"
age = 18
print(f"姓名: {name}, 年龄: {age}")
```

### 格式化数字
```python
price = 19.99
print(f"价格: {price:.2f}元")  # 保留2位小数
```

## 3. format方法

字符串的内置方法：

```python
name = "小明"
age = 18
print("姓名: {}, 年龄: {}".format(name, age))
```

## 4. %格式化（旧方法）

Python早期的格式化方法：

```python
name = "小明"
age = 18
print("姓名: %s, 年龄: %d" % (name, age))
```

## 5. 格式化符号

| 符号 | 说明 | 示例 |
|------|------|------|
| :.2f | 保留2位小数 | {price:.2f} |
| :.1% | 百分比 | {score:.1%} |
| :<10 | 左对齐 | {name:<10} |
| :>10 | 右对齐 | {age:>10} |
| :^10 | 居中 | {name:^10} |

## 6. 实践练习

```python
# 商品信息
name = "苹果"
price = 5.5
quantity = 3
total = price * quantity

print(f"商品: {name}")
print(f"单价: {price:.2f}元")
print(f"数量: {quantity}个")
print(f"总价: {total:.2f}元")
```

## 7. 总结

推荐使用f-string，简单易读！