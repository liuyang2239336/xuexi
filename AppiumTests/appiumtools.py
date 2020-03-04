from selenium.webdriver.support.ui import WebDriverWait

# 自定义的方法
def find_element(driver=None, locator=None, timeout=10):
    """
        名字：动态查找元素
        参数：
            driver: 浏览器的实例化对象
            locator: 元素定位的方法 ("id", "username") / ("xpath", "xxxxx") /("aid", "xxxxx") /("aui", "xxxxx")
                类型： 
                    ID = "id"
                    XPATH = "xpath"
                    accessibility_id = "aid"
                    android_uiautomator = "aui"
            timeout: 超时时间：默认10
    """

    if locator[0] == "aid":
        locator = ("accessibility id", locator[1])
    if locator[0] == "aui":
        locator = ("-android uiautomator", 'new UiSelector().text("{}")'.format(locator[1]))

    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))


def click(driver, locator):
    find_element(driver, locator).click()


def is_exsit(driver, locator):
    try:
        find_element(driver, locator)
        return True
    except:
        return False
