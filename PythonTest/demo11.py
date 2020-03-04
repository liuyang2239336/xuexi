class Father():
    name = "孩子他爹"
    rmb = 500

    def hava_kuang(self):
        print("他爹家有矿")

# 类的继承；被继承的父类，继承的类子类
class Son(Father):
    name = "别人家的孩子"
    rmb = 5

    def ta_ba_de(self):
        super().hava_kuang()

    def hava_kuang(self):
        print("被他儿子败光了！")

# 子类可以使用父类的成员方法和属性
s = Son()
print(s.rmb)

s.ta_ba_de()
# 重写
s.hava_kuang()
