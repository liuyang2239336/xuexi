# 包
import time # 导入包
import os
import random 


from hw02 import db  # 导入变量
from hw02 import reg   # 导入方法 
a = reg("test", "test")
print(a)

# 导入类
from demo10 import Person
p = Person("李小花", "女", 175, 50)
p.weight