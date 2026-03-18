# 模块基础

# 什么是模块？
# 模块是包含Python代码的文件，可以被其他程序导入使用

# 1. 导入模块
import math
print(f"圆周率: {math.pi}")
print()

# 2. 导入特定函数
from math import sqrt
print(f"平方根: {sqrt(16)}")
print()

# 3. 导入并重命名
import math as m
print(f"圆周率: {m.pi}")
print()

# 4. 导入所有（不推荐）
from math import *
print(f"圆周率: {pi}")
print()

# 5. 创建自己的模块
# 创建mymodule.py文件，定义函数和变量
# 然后在其他文件中导入使用

# 6. 查看模块内容
import math
print(dir(math))

# 7. 常用内置模块
import os        # 操作系统接口
import sys       # 系统相关
import random    # 随机数
import datetime  # 日期时间
import json      # JSON处理
