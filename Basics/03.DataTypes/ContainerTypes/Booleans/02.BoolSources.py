# 布尔值的来源

# 布尔值主要来自两种运算：比较运算和逻辑运算

# (1) 比较运算
# 比较运算符用于比较两个值的关系，返回布尔值

# 运算符	说明	   示例	           结果
#  ==	   等于	      3 == 5	     False
#  !=	  不等于      3 != 5	     True
#  >	   大于	      5 > 3	        True
#  <	   小于	      5 < 3	        False
#  >=	  大于或等于   5 >= 5	     True
#  <=	  小于或等于   5 <= 3	     False

# 示例：使用比较运算生成布尔值
age = 18
is_adult = age >= 18  # True（因为 18 >= 18）
print("is_adult =", is_adult)

# 其他比较示例
print("3 == 5 =", 3 == 5)  # 输出: False
print("3 != 5 =", 3 != 5)  # 输出: True
print("5 > 3 =", 5 > 3)    # 输出: True
print("5 < 3 =", 5 < 3)    # 输出: False

# (2) 逻辑运算
# 逻辑运算符用于组合或修改布尔值

# 运算符	说明	示例	结果
# and	逻辑与（都真）	True and False	False
# or	逻辑或（任一真）	True or False	True
# not	逻辑非（取反）	not True	False

# 示例：使用逻辑运算
has_money = True
has_time = False

can_travel = has_money and has_time  # False（必须同时满足）
can_relax = has_money or has_time    # True（只需满足一个）
is_busy = not has_time  # True（取反）

print("can_travel =", can_travel)
print("can_relax =", can_relax)
print("is_busy =", is_busy)