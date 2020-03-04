# 类的声明

# 类名首字母大写
class Person():
    # 年龄身高性别体重...
    # 成员变量：类里面的变量
    name = "张三"
    sex = "男"
    height = 175
    weight = 49

    # 构造方法：初始化成员变量
    def __init__(self, mz, xb, sg, tz):
        # 给成员变量赋值
        self.name = mz
        self.sex = xb
        self.height = sg
        self.weight = tz
        self.eat()

    # 功能：能干啥，吃、走路、说话...
    # self:固定的写法，类本身的对象
    # 成员方法
    def eat(self):
        print("人能吃")

    def talk(self, msg):
        print("人能说话{}".format(msg))

# 如何去使用:实例化-实例化对象
p = Person("李小花", "女", 175, 50)
print(p.name)
print(p.sex)
# p.eat()
p.talk("武汉加油！")
