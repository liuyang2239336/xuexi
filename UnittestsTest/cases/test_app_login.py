import unittest, time
from appium import webdriver
from utils.appiumtools import find_element, click, is_exsit


class TestCaseAppLogin(unittest.TestCase):
    

    def test_01_app_login(self):
        """
            这是登录方法
        """
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

        username = ("id", "com.allsaprk.dh.allspark:id/et_user")
        password = ("id", "com.allsaprk.dh.allspark:id/et_pass")
        loginbtn = ("id", "com.allsaprk.dh.allspark:id/bt_login")

        find_element(driver, username).send_keys("17781780824")
        find_element(driver, password).send_keys("1234")
        click(driver, loginbtn)

        time.sleep(3)
        try:
            assert ".activity.MainActivity" == driver.current_activity
            print("登录成功！")
        except:
            print("登录失败")


