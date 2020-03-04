from dbtools import DBTool

def login(username, password):

    # 判断输入的用户和密码是不是有问题
    if username == "" or password == "":
        return False

    # 去数据库查询用户表，用户是否是否存在
    db = DBTool()
    sql = "select * from tbl_user where username='{}'".format(username)
    res = db.query(sql) # 失败了：False，成功：结果了
    print(res)
    # 2. 判断数据库查询是否成功
    if res == False: # res=Flase：查询数据库失败了
        return False    # 登录失败，返回False
    else:   # 否则就是查询成功
        print(res)
        if len(res) == 0: # 没有找到该用户,登录失败
            return False
        else:# 有这个用户，判断密码是否一致
            if res[0][1] == password:
                return True          # 密码一致，登录成功，返回True
            else:
                return False        # 密码不一致，登录失败，返回False

un = input("请输入用户名:")
pw = input("请输入密码：")
res = login(un, pw)
if res == True:
    print("登录成功！")
else:
    print("登录失败！")