"""
    pymysql操作mysql数据库
"""
import pymysql


class DBTool():
    # 构造方法来初始化，数据库信息
    def __init__(self, host="127.0.0.1",username="root", password="123456", db="test"):
        # 用成员变量来存放这些信息
        self.db = db
        self.host = host
        self.username = username
        self.password = password

    def query(self, sql):
        """
            名字:查询方法
            参数：sql：查询的sql语句
            返回值：查询的结果：成功：结果；失败：返回False
        """
        try:
            db = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db)# 连接并且得到数据库的操作对象
            cursor = db.cursor() # 获取游标
            cursor.execute(sql)  # 执行查询语句
            res = cursor.fetchall() # 获取查询结果
            db.close()  # 关闭数据库连接
            return res
        except Exception as e:
            print(e)
            return False

    def commit(self, sql):
        """
            名字:增加/修改/删除方法
            参数：sql：查询的sql语句
            返回值：操作成功返回True/操作失败返回False
        """
        try:
            db = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db)# 连接并且得到数据库的操作对象
            cursor = db.cursor() # 获取游标
            cursor.execute(sql)  # 执行查询语句
            db.commit() # 提交修改
            db.close()  # 关闭数据库链接
            return True
        except Exception as e:
            print(e)
            return False

# d = DBTool()
# # res = d.query("self * from tbl_user")
# # sql里面出现引号：外双内单/外单内双
# # sql = 'INSERT INTO tbl_user VALUES("ljtest", "123456", "man", 18)'
# # sql = 'update tbl_user set age=108 where username="ljtest"'
# sql = 'delete from tbl_user where username="ljtest"'
# if d.commit(sql) == True:
#     print("添加成功")
# else:
#     print("添加失败")
