# 循环控制

# 1. break - 跳出整个循环
print("break示例:")
count = 0
while True:
    print(f"计数: {count}")
    count += 1
    if count >= 5:
        print("跳出循环")
        break
print("\n")

# 2. continue - 跳过本次循环
print("\ncontinue示例:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # 跳过偶数
        continue
    print(f"奇数: {num}")
print("\n")

# 3. else - 循环正常结束后执行
print("\nelse示例:")
count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1
else:
    print("循环正常结束")
print("\n")

# 4. else和break配合
print("\nelse和break示例:")
count = 0
while count < 10:
    if count == 3:
        print("遇到3，跳出循环")
        break
    print(f"计数: {count}")
    count += 1
else:
    print("循环正常结束（不会执行）")
print("\n")

# 示例：猜数字游戏
print("\n猜数字游戏:")
import random
target = random.randint(1, 10)
while True:
    guess = int(input("猜一个数字(1-10): "))
    if guess == target:
        print(f"恭喜！答案是{target}")
        break
    elif guess < target:
        print("太小了，再试一次")
    else:
        print("太大了，再试一次")
