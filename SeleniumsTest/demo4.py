from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://132.232.44.158:8080/ljindex/")

a = ("xpath", '//*[@id="lunbotu"]/div[1]/a/img')
find_element(driver, a).click()

print(driver.title)
# 切换新窗口
driver.switch_to_window(driver.window_handles[-1])
print(driver.title)