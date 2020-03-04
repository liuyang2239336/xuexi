# get方法
# 网址url

# 1. 导入requests

import requests

# url = "http://www.baidu.com/"       # 请求的网址/接口
# res = requests.get(url)             # requests.get(url) > response (响应头，body)
# print(res.text)                     # 打印响应的信息

# 请求测谈网的版本号地址
url = "http://192.144.148.91:2333/showversion"
res = requests.get(url)

# http状态码：判断接口能不能工作
# 断言:如果表达式成立=断言通过/不成立就报错
assert res.status_code == 200

# 判断接口功能是否正常
r = res.json() # 把返回值变成字典
assert r.get("status") == 200

print("接口测试通过！")
