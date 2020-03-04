import requests
import traceback
from dbtools import DBTool
from exceltools import read_excel

# 1. 读取Excel中的测试用例
datas = read_excel("测试用例.xlsx", "Sheet1")

for r in datas: # res=[[测试用例1], [测试用例2]]/ r=[[测试用例1]]
    print("="*100)
    # 2. 填数据来发请求
    t = r[1]    # 测试用例名字
    u = r[2]    # 接口地址
    if r[3] != '':
        d = eval(r[3])    # 数据,r[3]取出来是字符串，但是在后面需要获取username，要转成字典（str>dict)
        n = d["username"]   # 取用户名
    else:
        d = None
        n = ''
    m = r[4]    # 方法名字/get/post
    h = r[5]    # excel定义的状态码
    c = r[6]    # 返回信息
    res = requests.request(m, url=u, json=d)  # request方法更加智能，传get自动使用get/传post自动使用post
    try:
        # 断言
        assert res.status_code == h
        assert res.json()["status"] == c

        # 对比数据库
        db = DBTool(host="192.144.148.91", username="ljtest", password="123456", db="ljtestdb")
        sql = "select * from t_user where username='{}'".format(n)
        r = db.query(sql)
        assert r != False       # 为了判断数据库查询成功，如果不成功则数据查询失败，代码抛出异常
        assert len(r) != 0      # 为了判断数据库表里面存在这个用户

        print("【{}】执行成功！".format(t))
    except:
        traceback.print_exc()
        print("【{}】执行失败！".format(t))