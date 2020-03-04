# 把注册的功能改的mysql进行操作 》 pymysql
from dbtools import DBTool

def reg(username, password):
    if username == "" or password == "":
        print("用户名或密码格式不正确")
        return False   

    # 查询用户是否已经注册注册了
    db = DBTool()
    sql = "select * from tbl_user where username='{}'".format(username)

    if len(db.query(sql)) != 0:
        print("用户名已存在，不能重复注册！")
        return False
    else:
        sql = "INSERT INTO tbl_user VALUES('{}', '{}', 'f', 20)".format(username, password)
        if db.commit(sql) == True:
            print("注册成功！")
            return True
        else:
            print("注册失败！")
            return False

username = input("请输入用户名：")
password = input("请输入密码：")
res = reg(username, password)
print(res)
