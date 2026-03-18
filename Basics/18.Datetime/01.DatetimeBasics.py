# 日期基础

# 什么是日期？
# Python使用datetime模块处理日期和时间

from datetime import datetime, date, time

# 获取当前日期和时间
now = datetime.now()
print(f"当前时间: {now}")
print("\n")

# 获取当前日期
today = date.today()
print(f"今天: {today}")
print("\n")

# 创建日期对象
d = date(2024, 1, 1)
print(f"日期: {d}")
print("\n")

# 创建时间对象
t = time(12, 30, 45)
print(f"时间: {t}")
print("\n")

# 格式化日期
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"格式化: {formatted}")
print("\n")

# 解析日期字符串
date_str = "2024-01-01"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(f"解析: {parsed_date}")
print("\n")

# 日期计算
from datetime import timedelta
tomorrow = today + timedelta(days=1)
print(f"明天: {tomorrow}")
