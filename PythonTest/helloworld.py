print("hello world!")

# 用来输入内容的api，如果想要输入内容，就必须得用这个方法
"""
    这是多行注释
"""
# aa = input()        # aa = 输入的内容
# print(aa)

# python好简单




a = "python好简单呀！" # 字符串
# print(a)


b = 100 # 数字/整型
# print(b)

# bool类型
c = True
d = False
# print(c)
# print(d)

# 空类型，啥也木有，但是就是一个类型
e = None 
# print(e)

# 元组 ()
f = ()  # 空元组，它的类型是元组，但是元组里面木有东西
f = (1,2,3,4,5,6) # 元素和元素使用逗号隔开
f = (1,"python", True, None, f) # 元组的元素可以是任意类型的
# print(len("123"))         # 统计长度（元素的个数）
# print(f.count("python"))    # 统计元素出现的次数


name = "wangyao"
# print(name.count("w"))

# 下标：0开始数
# print(f.index("python")) # 下标为1，元素的位置应该+1


# list：数组
g = [1,2,3,4,5,6]
g = [1,"python", True, None, f]
# print(g)
# list增加
# g.append(1)
# g.append("123")
# g.append(True)
# print(g)
# g.remove("123")
# print(g)
g.insert(2,"代码有毒!")
ff = g.pop(1) # pop从list中删除元素，并且把删掉的元素返回出去
# print(ff)
print(g)

g[1] = "Python有毒!"
print(g)

# g.clear() # 清空元素

gg = [2,3,4,523,2,324,234,6,567,8,98,69]
gg.sort()
print(gg)

# 颠倒数组的顺序
gg.reverse()
print(gg)

# 字典： 接口测试json格式
# "username":key/键；"wangyao":value/值,他俩是一对儿，:隔开
users = {"username":"shuzhan", "gf":None}

# 取值
print(users.get("username1"))
users["bf"] = "xxx"
print(users["bf"])

users["gf"] = "sgn"

# 清空
# users.clear()
print(users)

# 初始化
x = None
x = {}