# lambda函数

# 什么是lambda函数？
# lambda是匿名函数，用于创建简单的单行函数

# 基本语法：lambda 参数: 表达式

# 示例1：基本用法
square = lambda x: x ** 2
print(f"5的平方: {square(5)}")
print("\n")

# 示例2：多个参数
add = lambda a, b: a + b
print(f"3 + 5 = {add(3, 5)}")
print("\n")

# 示例3：与map函数配合
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"平方: {squares}")
print("\n")

# 示例4：与filter函数配合
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {evens}")
print("\n")

# 示例5：与sorted函数配合
students = [
    {"name": "小明", "age": 18},
    {"name": "小红", "age": 20},
    {"name": "小刚", "age": 16}
]
sorted_students = sorted(students, key=lambda s: s["age"])
print(f"按年龄排序: {sorted_students}")
print("\n")

# 示例6：条件表达式
get_grade = lambda score: "及格" if score >= 60 else "不及格"
print(f"成绩85: {get_grade(85)}")
print(f"成绩55: {get_grade(55)}")
