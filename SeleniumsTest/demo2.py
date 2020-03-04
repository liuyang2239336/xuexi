import time
from selenium import webdriver


# 1. 打开浏览器:固定的/ 获取浏览器句柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 2. 输入并访问网址
driver.get("http://localhost:8080/test/")

driver.find_element_by_link_text("点我就送251天免费套餐+10W！").click()

time.sleep(3)
# driver.switch_to_alert().accept() # 确定按钮
driver.switch_to_alert().dismiss() # 取消按钮