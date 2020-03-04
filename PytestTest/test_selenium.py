import pytest
from selenium import webdriver
from seleniumtools import find_element


def test_01_index():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.maximize_window()
    driver.get("http://132.232.44.158:8080/ljindex")

    search_input = ("xpath", '/html/body/div[1]/div/div[1]/div/input')
    find_element(driver, search_input).send_keys("123")
    