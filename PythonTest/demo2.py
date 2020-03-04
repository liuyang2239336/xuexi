
for i in range(10): # range(10) = (0,1,2,3,4,5,6,7,8,9)
    print(i)
    # print("python好简单啊！")

# 遍历str/()/[]/{}

# 1.字符串str
a = "阿斯顿发加拉三等奖法拉时代峻峰"
for i in a:
    print(i)

a = (1, "xx", 2, "00", None)
for i in a :
    print(i)

a = [1, "xx", 2, "00", None]
for i in a :
    print(i)

# 循环字典第一种方式
a = {"username":"test", "password":"123456"}
for i in a :
    print(i)
    print(a.get(i))
    print(a[i])

# 通过key和value来进行遍历
for k,v in a.items():
    print("{}->{}".format(k, v))


z = "好难啊"
x = "是真的"
print("python",z)
print("python"+z)
print("{}python{}".format(x,z))


