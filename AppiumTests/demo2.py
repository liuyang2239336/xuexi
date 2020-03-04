from appium import webdriver
from appiumtools import find_element, click, is_exsit



desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'vivo x6plus d'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis'               # app的名字：
                                                        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                        # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = '.ApiDemos'              # 同上↑
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) # 打开指定手机里面的软件；driver=定位软件的句柄


# 1. accessibility id
# driver.find_element_by_accessibility_id('Accessibility').click()

# # 2. xpath
# driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Custom View"]').click()

# 3. id > resource_id
# driver.find_element_by_id('android:id/text1').click()

# 4. 文本值
# driver.find_element_by_android_uiautomator('new UiSelector().text("App")').click()

app = ("aui", "App")
search = ("aui", "Search")
invoke_search = ("aui", "Invoke Search")
datas = ("id", "io.appium.android.apis:id/txt_query_prefill")
# find_element(driver, app).click()
# assert shifoucunzai("Search") == True

app_text = find_element(driver, app).text
print(app_text)

click(driver, app)
click(driver, search)
click(driver, invoke_search)
find_element(driver, datas).send_keys("我不要当点点点！")
find_element(driver, datas).clear()

# assert is_exsit(driver, search) == True

driver.quit()

