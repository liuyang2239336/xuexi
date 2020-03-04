# -*- coding: utf-8 -*-

"""
    Jython没有提示
"""
import time

# 导入必须要的包
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# 连接安卓手机
device = MonkeyRunner.waitForConnection()

# 打开app
app = "com.allsaprk.dh.allspark/.activity.LoginActivity"
device.startActivity(component=app)

# 点一下这个坐标点
device.touch(219, 716, MonkeyDevice.DOWN_AND_UP)
time.sleep(1)
device.type("17781780824")


device.touch(236, 876, MonkeyDevice.DOWN_AND_UP)
time.sleep(1)
device.type("1234")

device.touch(447, 1264, MonkeyDevice.DOWN_AND_UP)
