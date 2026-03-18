# 正则表达式教程.md

# Python 正则表达式教程

## 1. 什么是正则表达式？

正则表达式是用于匹配字符串模式的工具。

## 2. 基本用法

```python
import re

# 匹配
match = re.match(r"hello", "hello world")

# 搜索
search = re.search(r"hello", "say hello")

# 查找所有
matches = re.findall(r"hello", "hello world, hello python")

# 替换
new_text = re.sub(r"hello", "hi", "hello world")
```

## 3. 常用模式

- \d - 数字
- \w - 字母数字下划线
- \s - 空白字符
- . - 任意字符
- * - 0次或多次
- + - 1次或多次

## 4. 总结

正则表达式用于字符串匹配！