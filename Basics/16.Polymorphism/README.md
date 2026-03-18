# 多态教程.md

# Python 多态教程 

## 1. 什么是多态？

多态是指不同的对象对同一方法有不同的响应。

## 2. 示例

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵喵"

def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_speak(dog)  # 汪汪汪
animal_speak(cat)  # 喵喵喵
```

## 3. 总结

多态让代码更灵活！