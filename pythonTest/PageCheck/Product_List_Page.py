import allure

from BaseTools.BasePage import *


class ProductListPage(BasePage):
    _loc_jjtg = '//*[@id="qggsdzt"]/a'  # 基金投顾
    _loc_jxcp = '//*[@id="qggjjcp"]/a'  # 精选产品
    _loc_hqzq = '//*[@id="container"]/div/div[2]/div/div[2]/div[1]/div[1]'  # 活期专区
    _loc_jjzq = '//*[@id="container"]/div/div[2]/div/div[2]/div[1]/div[3]'  # 基金专区
    # 为您精选中第一个购买按钮
    _loc_first_purchase_btn = '//*[@id="container"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[3]/button'
    # 为您精选中第二个购买按钮
    _loc_sec_purchase_btn = '//*[@id="container"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]/button'

    @allure.step("点击基金投顾")
    def click_jjtg(self):
        self.jjtg.click()

    @allure.step("点击精选产品")
    def click_jxcp(self):
        self.jxcp.click()

    @allure.step("活期专区")
    def click_hqzq(self):
        self.hqzq.click()

    @allure.step("基金专区")
    def click_jjzq(self):
        self.jjzq.click()

    @allure.step("点击为您精选中第一个购买按钮")
    def click_first_purchase_btn(self):
        self.first_purchase_btn.click()

    @allure.step("点击为您精选中第二个购买按钮")
    def click_sec_purchase_btn(self):
        self.sec_purchase_btn.click()
