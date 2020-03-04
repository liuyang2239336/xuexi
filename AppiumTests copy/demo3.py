"""
    按键操作
"""

import time
from appium import webdriver
from appiumtools import find_element, click, is_exsit

desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'vivo x6plus d'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'com.allsaprk.dh.allspark'               # app的名字：
                                                        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                        # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = '.activity.LoginActivity'              # 同上↑
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) # 打开指定手机里面的软件；driver=定位软件的句柄


# 按键
# driver.back()
# driver.press_keycode(4)
# driver.press_keycode(4)
driver.press_keycode(3)


# 滑动
for i in range(10):
    time.sleep(1)
    driver.swipe(163, 912, 717, 901)
    time.sleep(1)
    driver.swipe(717, 912, 163, 901)
