# 1. 输入用户名和密码

# 2. 去判断登录是否成功- 如果登录成功-打印登录成功；反之，打印失败！

# 能够看懂就可以
username = input("请输入用户名:")
password = input("请输入密码：")

if username == "" and password == "":
    print("用户名或者面不能为空！")
    exit() # 退出程序

# db的作用就是模拟数据
db = {"username":"test", "password":"test"}

# 如何去判断输入的密码和db里面的密码一致
if username == db.get("username") and password == db.get("password"):
    print("登录成功！")
else:
    print("登录失败!")