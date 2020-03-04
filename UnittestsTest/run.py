"""
    整个工具/框架的运行入口
"""
import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 1. 加载所有的测试用例
# 使用unittest自带loader去动态查找cases文件下下面的以test_开头、.py结尾的测试用例
t = unittest.defaultTestLoader.discover('cases', 'test_*.py')

# 2. 运行所有的测试用例，并且自动生成测试报告

title = "测试报告"
descr = "测试报告描述"
report = "./reports/report.html" # .html exe apk dmg..

with open(report, "wb") as f:               # 创建一个report变量路径里面的文件，如果存在该文件那就替换，不存在就新建一个
    runner = HTMLTestRunner(stream=f, title=title, description=descr)   # 初始化htmltestrunner
    runner.run(t)                                                       # 使用run方法运行所有的测试用例
