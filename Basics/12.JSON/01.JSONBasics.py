# JSON基础

# 什么是JSON？
# JSON是一种数据交换格式，常用于网络数据传输

import json

# 1. Python字典转JSON字符串
student = {
    "name": "小明",
    "age": 18,
    "city": "北京"
}

json_str = json.dumps(student, ensure_ascii=False)
print(f"JSON字符串: {json_str}")
print("\n")

# 2. JSON字符串转Python字典
json_str = '{"name": "小红", "age": 20}'
python_dict = json.loads(json_str)
print(f"Python字典: {python_dict}")
print("\n")

# 3. 写入JSON文件
data = {
    "students": [
        {"name": "小明", "age": 18},
        {"name": "小红", "age": 20}
    ]
}

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 4. 读取JSON文件
with open("students.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(f"读取的数据: {loaded_data}")
print("\n")

# 5. 格式化JSON
json_str = json.dumps(student, ensure_ascii=False, indent=2)
print(f"格式化JSON:\n{json_str}")
