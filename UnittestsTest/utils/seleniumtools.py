from selenium.webdriver.support.ui import WebDriverWait

# 自定义的方法
def find_element(driver=None, locator=None, timeout=10):
    """
        名字：动态查找元素
        参数：
            driver: 浏览器的实例化对象
            locator: 元素定位的方法 ("id", "username") / ("xpath", "xxxxx")
                类型： 
                    ID = "id"
                    NAME = "name"
                    XPATH = "xpath"
                    TAG_NAME = "tag name"
                    LINK_TEXT = "link text"
                    CLASS_NAME = "class name"
                    CSS_SELECTOR = "css selector"
                    PARTIAL_LINK_TEXT = "partial link text"
            timeout: 超时时间：默认10
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))