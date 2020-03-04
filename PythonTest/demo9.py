a = [1,2,3,4,5,6]
print(a[0])
print(a[1])

# 异常处理，如果代码没有报错，就包try里面的代码运行完，如果报错了呢，去执行except的代码
# 增加代码的健壮性：报错之后也能运行
# try > （报错-except/没有报错-else）> finally; else和finally可选的
try:
    print(a[1])
except:
    print("这个代码报错了！")
else:
    print("并没有报错")
finally:
    print("最终执行了finally")



print("aklsdjflkasjdlkfjasld")
print("aklsdjflkasjdlkfjasld")
print("aklsdjflkasjdlkfjasld")
print("aklsdjflkasjdlkfjasld")

