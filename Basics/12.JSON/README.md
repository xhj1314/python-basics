# JSON教程.md

# Python JSON教程 

## 1. 什么是JSON？

JSON是一种数据交换格式，常用于网络数据传输。

## 2. Python字典转JSON

```python
import json

student = {"name": "小明", "age": 18}
json_str = json.dumps(student, ensure_ascii=False)
print(json_str)
```

## 3. JSON转Python字典

```python
json_str = '{"name": "小红", "age": 20}'
python_dict = json.loads(json_str)
print(python_dict)
```

## 4. 读写JSON文件

```python
# 写入
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

## 5. 总结

JSON是数据交换的标准格式！