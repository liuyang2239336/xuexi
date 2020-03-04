# import time
# time.sleep(1)

# from selenium import webdriver


# 声明方法：咋写
def add(a, b):
    sum = a + b
    return sum

def add1(a,b,c,d):
    return a+b+c+d

# 调用方法
c = add(1,1)
d = add(3,54)

print(c)
print(d)


def test():
    print("sadlfkjalsd")
    print("sadlfkjalsd")
    print("sadlfkjalsd")
    print("sadlfkjalsd")

test()

# 参数的默认值
def add2(a=1, b=2):
    return a + b
    
print(add2())
print(add2(10,10))
print(add2(b=10,a=20))