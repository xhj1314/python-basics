# 迭代基础

# 什么是迭代？
# 迭代是遍历序列中每个元素的过程

# 1. 可迭代对象
fruits = ["苹果", "香蕉", "橙子"]

# 使用for循环迭代
for fruit in fruits:
    print(fruit)
print("\n")

# 2. 迭代器
iterator = iter(fruits)
print(next(iterator))  # 苹果
print(next(iterator))  # 香蕉
print(next(iterator))  # 橙子
print("\n")

# 3. 创建迭代器
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current - 1
        raise StopIteration

counter = Counter(0, 5)
for num in counter:
    print(num)
print("\n")

# 4. 生成器
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
