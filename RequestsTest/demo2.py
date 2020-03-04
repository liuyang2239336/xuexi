import requests
import traceback
from dbtools import DBTool

u = "http://192.144.148.91:2333/login"
d = {"username":"liuyang233","password":"liu222222"}
res = requests.post(url=u, json=d)      # url=u:指定url使用u参数

try:
    # 断言
    assert res.status_code == 200
    assert res.json()["status"] == 200

    # 对比数据库
    db = DBTool(host="192.144.148.91", username="ljtest", password="123456", db="ljtestdb")
    sql = "select * from t_user where username='{}'".format(d["username"])
    r = db.query(sql)
    assert r != False       # 为了判断数据库查询成功，如果不成功则数据查询失败，代码抛出异常
    assert len(r) != 0      # 为了判断数据库表里面存在这个用户

    print("测试用例执行成功！")
except:
    traceback.print_exc()
    print("测试用例执行失败！")