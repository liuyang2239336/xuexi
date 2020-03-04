
from utils.seleniumtools import find_element

class PageRegist():
    def __init__(self, driver):
        """
            封装好所有要用的元素
        """
        self.url = "http://132.232.44.158:8080/ljindex/html/register.html"
        self.title = "注册"
        self.username = ("id", "username")
        self.password = ("id", "password")
        self.confirpw = ("id", "confirpw")
        self.phonenum = ("id", "phonenum")
        self.emailnum = ("id", "emailnum")
        self.useregis = ("id", "userRegist")
        self.driver = driver
        
    def regist(self, username, password, confirpw, phonenum, emailnum):
        """
            用户注册的步骤
        """
        find_element(self.driver, self.username).send_keys(username)
        find_element(self.driver, self.phonenum).send_keys(phonenum)
        find_element(self.driver, self.password).send_keys(password)
        find_element(self.driver, self.confirpw).send_keys(confirpw)
        find_element(self.driver, self.emailnum).send_keys(emailnum)
        find_element(self.driver, self.useregis).click()
