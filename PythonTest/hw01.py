# user数据
db = [{"username":"zhangxinyue", "password":"test", "age":18, "weight":49}]
# 输入用户名和密码
username = input("请输入用户名：")
password = input("请输入密码：")

# 判断用户名和不为空
if username == "" or password == "":
    print("用户名或密码不能为空！")
    exit()

# 判断是否用户是否存在
for user in db:
    if user.get("username") == username:
        print("用户名已存在！")
        exit()

# 如果执行到这儿，那就说明，db里面的字典都循环完了-》没有重复的用户名
# u = {}
# u["username"] = username
# u["password"] = password
# u["age"] = 18
# u["weight"] = 49
# db.append(u)
u = {"username":username, "password":password, "age":18, "weight":49}
db.append(u)
print(db)

# 输入一个字典，输出list
result = []
a = {"username":"zhangxinyue", "password":"test", "age":18, "weight":49}
for i in a:
    result.append(i)
    result.append(a[i])

print(result)

