# 导入pytest

import pytest
import requests
from dbtools import DBTool


# 每个方法就是一个测试用例
def test_01_login():
    # 构造请求
    u = "http://192.144.148.91:2333/login"
    d = {"username":"liuyun1", "password":"a12345678"}
    res = requests.post(url=u, json=d)
    # 断言
    assert res.status_code == 200
    assert res.json()["status"] == 200
    # 查询数据库
    db = DBTool(host="192.144.148.91", username="ljtest", password="123456", db="ljtestdb")
    sql = "select * from t_user where username='{}'".format(d["username"])
    r = db.query(sql)
    assert len(r) != 0
    print("测试通过！")