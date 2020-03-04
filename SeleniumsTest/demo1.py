import time
from selenium import webdriver


# 1. 打开浏览器:固定的/ 获取浏览器句柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 2. 输入并访问网址
driver.get("http://132.232.44.158:8080/ljindex/")

# # 3. 开始操作网页

# # xpath定位
e = driver.find_element_by_xpath('//*[@id="unlogin"]/div[1]/a')
e.click()
time.sleep(3)
# id定位
driver.find_element_by_id('username').send_keys("liuyun")
driver.find_element_by_id('password').send_keys("123456711")
driver.find_element_by_id('userLogin').click()

url = driver.current_url
title = driver.title
print(title)
print(url)


# driver.get("https://www.baidu.com/")
# # driver.find_element_by_name("wd").send_keys("python")
# # driver.find_element_by_class_name('s_ipt').send_keys("python")
# # driver.find_element_by_css_selector('#kw').send_keys('python')
# # driver.find_element_by_link_text('抗击肺炎').click() # 只能超链接
# # driver.find_element_by_partial_link_text('抗击肺').click()# 只能超链接
# driver.find_element_by_tag_name('a')

# # 退出测试
driver.quit()