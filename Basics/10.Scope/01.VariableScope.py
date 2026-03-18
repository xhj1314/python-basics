# 变量作用域

# 什么是作用域？
# 作用域是变量的有效范围

# 1. 局部变量 - 在函数内部定义的变量
def my_function():
    local_var = 10  # 局部变量
    print(f"局部变量: {local_var}")

my_function()
# print(local_var)  # 错误！局部变量在函数外不可访问
print()

# 2. 全局变量 - 在函数外部定义的变量
global_var = 100  # 全局变量

def my_function2():
    print(f"全局变量: {global_var}")

my_function2()
print()

# 3. 在函数内修改全局变量
count = 0

def increment():
    global count  # 声明使用全局变量
    count += 1

increment()
print(f"count: {count}")  # 1
print()

# 4. 嵌套函数的作用域
def outer():
    x = 10
    
    def inner():
        nonlocal x  # 声明使用外层函数的变量
        x = 20
    
    inner()
    print(f"x: {x}")  # 20

outer()
