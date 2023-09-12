import allure

from BaseTools.BasePage import *


class HomeWithOutLogin(BasePage):
    _loc_loginbtn = '//*[@id="container"]/div/div[1]/div/div[1]/div[3]/div/div[3]'  # 立即登录按钮
    _loc_logonbtn = '//*[@id="container"]/div/div[1]/div/div[1]/div[3]/div/div[4]'  # 免费注册按钮
    _loc_onlinebtn = '//*[@id="footerCustomOnLine"]'  # 在线客服按钮
    _loc_fastlogin = '/html/body/div[1]/div[2]/div/div[2]/a[1]'  # 顶部快速登录
    _loc_logon = '/html/body/div[1]/div[2]/div/div[2]/a[2]'  # 顶部免费注册

    # 检查页面元素是否存在
    @allure.step("检查页面元素是否存在")
    def check(self):
        self.loginbtn
        self.logonbtn
        self.onlinebtn
        self.fastlogin
        self.logon

    # 点击登录按钮
    @allure.step("点击登录按钮")
    def click_login(self):
        self.loginbtn.click()
        logger.info("已点击按钮： loginbtn")

    # 点击注册按钮
    @allure.step("点击注册按钮")
    def click_logon(self):
        self.logonbtn.click()
        logger.info("已点击按钮： logonbtn")
