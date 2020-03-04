# 计算第几天
y = int(input("请输入年份:")) # 类型转换：把str转成int
m = int(input("请输入月份:"))
d = int(input("请输入号数:"))
days = [31,28,31,30,31,30,31,31,30,31,30,31] # 平年的天数
# 闰年
if y%4 == 0 and y%100!=0 or y%400==0:
    print("执行了闰年！")
    days[1] = 29
# 加天数 m=2 > 1月+号数; m=10> 1-9月+天数 (day[0]-day[8])
# sum = d
for i in range(m-1): # 要生成长度是多少
    print("第{}次运行".format(i))
    print(d)                    # i=0/d=1;i=1/d=29+1;i=2;d=31+30
    d = days[i] + d

print(d)
# print("{}-{}-{}是今年的第{}天".format(y, m, d, sum))