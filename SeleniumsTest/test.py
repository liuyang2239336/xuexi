import time
from selenium import webdriver

# 1. 打开浏览器:固定的/ 获取浏览器句柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 2. 输入并访问网址
driver.get("http://132.232.44.158:8080/ljindex")


driver.find_element_by_link_text("注册").click()

time.sleep(5)
driver.find_element_by_id("userRegist").click()

time.sleep(3)
driver.switch_to_alert().accept()
