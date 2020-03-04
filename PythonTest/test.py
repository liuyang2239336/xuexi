

# 生成10万条数据

# 把数据写到datas.txt


datas = []
for i in range(1, 100000):
    username = "robot{}".format(10219 + i)
    password = "a12345678"
    usermail = "god{}@qq.com".format(10785 + i)
    userphon = 13700010120 + i

    datas.append("{},{},{},{}\n".format(username, password,usermail, userphon))

with open("./datas.txt", "w+") as f :
    for i in datas:
        f.write(i)

