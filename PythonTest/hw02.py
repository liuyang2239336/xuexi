db = [{"username":"zhangxinyue", "password":"test", "age":18, "weight":49}]
def reg(username, password):
    """
        名称：注册方法
        参数：username, password
        返回值：True：成功/ False：失败
    """
    # 判断用户名和密码是否为空
    if username == "" or password == "":
        print("注册失败，用户名和密码有空值!")
        return False

    # 判断用户名是否已经存在
    for user in db:
        if user.get("username") == username:
            print("注册失败，用户名已存在")
            return False

    # 所有的用户名不存在
    user = {"username":username, "password":password, "age":18, "weight":49}
    db.append(user)

    print("注册成功！")
    return True

# 调用方法：方法必须在调用的前面
username = input("请输入用户名：")
password = input("请输入密码：")
res = reg(username, password)
print(db)
print(res)
    

    