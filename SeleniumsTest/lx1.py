import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://132.232.44.158:8080/ljindex/")
driver.find_element_by_xpath('//*[@id="unlogin"]/div[1]/a').click() # 登录

# 等待3秒
time.sleep(3)

driver.find_element_by_id('username').send_keys("liuyun")
driver.find_element_by_id('password').send_keys("12345678")
driver.find_element_by_id('userLogin').click()

# 断言
time.sleep(3)
try:
    assert driver.title == "测谈网"
    print("登录成功")
except:
    print("登录失败")