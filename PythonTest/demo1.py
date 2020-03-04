# a = input("请输入舒展是不是直男，1：是；0：不是：")
# a的变量类型


# 判断； == 判断语句：判断a是否等于1，如果a等于1：打扰了！如果不等于1：你好呀
# 缩进：if/while/for/def/class/try...
# if a == "1":
#     print("打扰了！")
# else:
#     print("你好呀~")

# 不等于
c = 10
if c != 18:
    print("这个c不是18！")
    
if c > 18:
    print("这个c就已经成年了！")

if c < 18:
    print("这个c未成年！")
    
c = 10
d = 10
if c is not d:
    print("c和d的类型不一样")
else:
    print("一样")


f = "python"
g = "i love java"
if f not in g:
    print("f在g里面木有出现！")
else:
    print("有出现")


a = 1
b = 2
c = 1

if a<b or b<c:
    print("条件成立")