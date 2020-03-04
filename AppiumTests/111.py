'''
def creattext(value,x):
    with open("data2.txt","a") as f:
        f.write(value)


b = "a12345678"

for i in range(100000,200000):
    
    creattext("liu{},{},13118{},abc{}@qq.com\n".format(i,b,i,i),"a")
'''


