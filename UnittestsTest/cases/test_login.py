# 类来实现测试用例
import unittest, time
from selenium import webdriver

# 登录模块
class TestCaseLogin(unittest.TestCase):

    # 每个成员方法就是固定的测试用例
    def test_01_login_success(self):
        driver = webdriver.Chrome(executable_path="drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get("http://132.232.44.158:8080/ljindex")
        driver.find_element_by_link_text("登录").click()
        time.sleep(3)

        driver.find_element_by_id("username").send_keys("liuyun1")
        driver.find_element_by_id("password").send_keys("a12345678")
        driver.find_element_by_id("userLogin").click()

        #断言
        time.sleep(3)
        # assert driver.title == "测谈网"
        self.assertEqual(driver.title, "测谈网") # 表示是否想等
        driver.quit()


    def test_02_failed(self):
        # assert 1==2
        self.assertEqual(1, 2)


    def test_03_error(self):
        pass