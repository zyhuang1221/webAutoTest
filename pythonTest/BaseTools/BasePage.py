import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import logging

# 创建log对象
logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self._driver = driver
        self._wait = WebDriverWait(driver, 30)
        sleep(1)
        logger.info("已进入页面： " + self._driver.current_url)

    def __getattr__(self, item):
        key = f"_loc_" + item
        xpath = getattr(self, key, None)
        # if self.__locator(xpath):
        #     # 根据xpath定位元素
        #     return self.get_element(xpath)
        # raise AttributeError("元素不存在: " + xpath)
        return self.__locator(xpath)

    # 检验元素是否存在
    def __locator(self, xpath):
        count = 1
        while True:
            path = True
            count += 1
            try:
                element = self._driver.find_element(By.XPATH, xpath)
            except Exception:
                sleep(1)
                logger.info("找不到元素" + xpath)
                path = False
            if path == True:
                logger.info("已找到元素，跳出循环" + xpath)
                return element
            elif count >= 10:
                logger.info("寻找元素大于10秒，跳出循环" + xpath)
                assert False, "元素'" + xpath + "'不存在"

    # 元素定位，自动进行等待
    def get_element(self, xpath):
        el = self._wait.until(
            visibility_of_element_located(
                (
                    By.XPATH,
                    xpath,
                )
            )
        )
        return el

    # 等待弹窗出现并确认
    def alert_ok(self):
        alert = self._wait.until(alert_is_present())
        alert.accept()


# class LoginPage(BasePage):
#     _loc_logbtn = '//div[@class="login"]'
#     _loc_username = '//*[@id="loginPhone"]'
#     _loc_password = '//*[@id="login"]/div[1]/div[1]/div[3]/div[1]/input'
#     _loc_check = '//*[@id="check_Login"]'
#     _loc_btn = '//*[@id="login"]/div[1]/div[1]/div[6]'
#     _loc_texts = '/html/body/div[1]/div[1]/div[2]/div/div[2]/span'
#
#     def login(self, username, password):
#         self.logbtn.click()
#         self.username.send_keys(username)
#         self.password.send_keys(password)
#         self.check.click()
#         self.btn.click()
#         assert "，欢迎来到中欧财富！" == self.texts.text

