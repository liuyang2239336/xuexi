import time
from selenium import webdriver
from seleniumtools import find_element

# 1. 打开浏览器:固定的/ 获取浏览器句柄
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.maximize_window()
for i in range(1000):
    # 2. 输入并访问网址
    driver.get('http://132.232.44.158:8080/ljindex/')

    userreg = ('xpath','//*[@id="unlogin"]/div[2]/a')
    username= ('xpath',"/html//input[@id='username']")
    phonenum= ('xpath',"/html//input[@id='phonenum']")
    emailnum= ('xpath',"/html//input[@id='emailnum']")
    confirpw = ('id','confirpw')
    password= ('xpath',"/html//input[@id='password']")
    userRegist = ('id','userRegist')

    find_element(driver,userreg).click()
    find_element(driver,username).send_keys('adgsa')
    find_element(driver,phonenum).send_keys('1s23213f23r1')
    find_element(driver,emailnum).send_keys('2safd232313')
    find_element(driver,password).send_keys('ae32113')

    # 判断有没有值
    a = find_element(driver,username).get_attribute('value')
    b = find_element(driver,phonenum).get_attribute('value')
    c = find_element(driver,emailnum).get_attribute('value')
    d = find_element(driver,password).get_attribute('value')
    if a == "" or b == "" or c == "" or d == "":
        print("第{}次出现了空值".format(i+1))

