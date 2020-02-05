'''
print("hello world")
print(233,"哈哈哈",1,2,3,2,2,2,2,"233")
print("haha"+"11")
print(11*20)
#变量 赋值
num = 2333
print(num)
a = int(input("请输入："))
b = int(input("请输入："))
c = print("和:",a+b)
c = ('哈哈',2,1,1,3,4,5,6,"哈哈",'哈哈','哈哈')
print(c[7],c[2])
print(c[0:8])
print(c.index('哈哈'))#显示第一个哈哈下标
print(c.count('哈哈'))#统计某个元素的数量
print(len(c))

a = ((1,'张三'),(2,'李四'))
print(a[1][1])

a = [1,2,3,4,'haha','hehe',[1,2,3],'haha']
print(a[-2][1])
print (len(a))
print(a.index('hehe'))
print(a.count('haha'))
a.append('gaga')
a.insert(0,'wawa')

print(a.pop(-1))
print(a)
a.extend('今天戴口罩了吗')
print(a)
del a[-1]
print(a)




a = {}
a["name"]="liu"
a['name2']='111'
a.update(sex="nan")

print(a)

a = 10
if a > 10:
    print("大于10")
else:
    print("哈哈")



if a > 10:
    print()

age = int(input('请输入你的年龄：'))
if age > 10 and age < 18:
    print("你不是小屁孩了")
elif age >= 18 and age <= 24:
    print("好好读大学")
elif age < 60 and age > 24:
    print("好好工作")
else:
    print("小屁孩")
print('结束！')

a = [1,2,3,4,5,6,7,8,9]
num = 0
for i in a:
    num = num + i
    print(num)
print(num)




db = {"username":"liuyang233","password":"123456"}
a = input("请输入用户名：")
b = input("请输入密码：")
if a == "" or b == "":
    print("参数不能为空")
    exit()
elif a == db.get("username"):
    print("用户名已存在请重新输入：")
    exit()
else:
    db["username"] = a
    db["password"] = b 
    print(db)
    '''



    

