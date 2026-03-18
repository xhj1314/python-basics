# 继承教程.md

# Python 继承教程 

## 1. 什么是继承？

继承允许一个类获得另一个类的属性和方法。

## 2. 基本用法

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):  # 继承Animal
    def speak(self):
        print(f"{self.name}汪汪汪")
```

## 3. 重写方法

```python
class Dog(Animal):
    def speak(self):  # 重写父类方法
        print(f"{self.name}汪汪汪")
```

## 4. 使用super()

```python
class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # 调用父类方法
        self.color = color
```

## 5. 总结

继承实现代码复用！