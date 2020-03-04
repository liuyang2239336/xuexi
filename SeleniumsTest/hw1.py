import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://132.232.44.158:8080/ljindex/index.html")

driver.find_element_by_xpath('//*[@id="unlogin"]/div[2]/a').click()

# time.sleep(3)
driver.implicitly_wait(10)      # 10秒内如果网页加载完成，那就去执行下面的代码

driver.find_element_by_id("username").send_keys("liuyun4")
driver.find_element_by_id("phonenum").send_keys("13990099823")
driver.find_element_by_id("password").send_keys("a12345678")
driver.find_element_by_id("confirpw").send_keys("a12345678")
driver.find_element_by_id("emailnum").send_keys("12345632@qq.com")
driver.find_element_by_id("userRegist").click()

time.sleep(3)
# driver.implicitly_wait(10)
# 弹出窗
driver.switch_to_alert().accept() # 点击提示语的确定按钮
# time.sleep(3)
driver.implicitly_wait(10)
try:
    assert driver.title == "登录"
    print("注册成功")
except:
    print("注册失败")