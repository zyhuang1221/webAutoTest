import allure

from BaseTools.BasePage import *


class MyAccountPage(BasePage):
    _loc_welcomeText = '/html/body/div[1]/div[1]/div[2]/div/div[2]/span'  # 登陆后的欢迎登陆文字
    _loc_jjtg = '//*[@id="qggsdzt"]/a'  # 基金投顾
    _loc_jxcp = '//*[@id="qggjjcp"]/a'  # 精选产品

    @allure.step("校验登录状态")
    def checkLoginStatus(self):
        assert self.welcomeText.text == "，欢迎来到中欧财富！", "登录校验失败"

    @allure.step("点击基金投顾")
    def click_jjtg(self):
        self.jjtg.click()

    @allure.step("点击精选产品")
    def click_jxcp(self):
        self.jxcp.click()
