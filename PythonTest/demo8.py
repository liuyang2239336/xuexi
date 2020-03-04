# 登录方法支持传入用户名和密码，登录成功返回值true，登录失败返回false
def login(username, password):
    if username == "" or password == "":
        return False

    # db的作用就是模拟数据
    db = {"username":"test", "password":"test"}

    # 如何去判断输入的密码和db里面的密码一致
    if username == db.get("username") and password == db.get("password"):
        return True
    else:
        return False

un = input("请输入用户名:")
pw = input("请输入密码：")
res = login(un, pw)
if res == True:
    print("登录成功，页面跳转到个人中心！")
else:
    print("登录失败，页面提示错误！")


abc = [1,2,3,4,5]
print(abc[0])
print(abc[1])
print(abc[-1])


