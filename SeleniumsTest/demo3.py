from selenium import webdriver
from seleniumtools import find_element


# 1. 打开浏览器:固定的/ 获取浏览器句柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 2. 输入并访问网址
driver.get("https://passport2.eastmoney.com/pub/login")



# 切换作用域到frame
frame = ("id", "frame_login")
e = find_element(driver, frame)
driver.switch_to_frame(e)

password_login = ("xpath", "/html/body/div/div[1]/span[1]")
find_element(driver, password_login).click()

username = ("id", "txt_account")
find_element(driver, username).send_keys("13990099999")


# 作用域切换回父网页
driver.switch_to_default_content()

mianfei = ("link text", "东方财富网免费版")
find_element(driver, mianfei).click()