a = input("请输入是否需要循环，0不需要1需要：")

# 死循环：一直执行，不退出！
# 退出while：
# 1. a != "1"
# break:退出循环

while a == "1":
    print("我去前面探探路，正在报道！")
    a = 2
    # break

# continue:跳出单次循环

for a in range(10):
    if a == 5:
        continue
    print("第{}次循环".format(a))

