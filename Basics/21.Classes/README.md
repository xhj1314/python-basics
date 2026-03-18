# 类教程.md

# Python 类教程 

## 1. 什么是类？

类是对象的模板，定义了对象的属性和方法。

## 2. 定义类

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"我叫{self.name}, 今年{self.age}岁")
```

## 3. 创建对象

```python
person = Person("小明", 18)
person.introduce()
```

## 4. 访问属性

```python
print(person.name)
person.age = 19
```

## 5. 总结

类是面向对象编程的基础！