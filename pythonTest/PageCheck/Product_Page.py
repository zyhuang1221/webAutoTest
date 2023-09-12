import allure

from BaseTools.BasePage import *


class ProductPage(BasePage):
    _loc_purchase_amt = '//*[@id="container"]/div[1]/div[3]/div[2]/div[4]/dl/dd/input'
    _loc_purchase_btn = '//*[@id="container"]/div[1]/div[3]/div[2]/div[4]/dl/dd/div[5]/a[1]'

    @allure.step("输入申购金额")
    def input_amt(self, amt):
        self.purchase_amt.send_keys(amt)

    @allure.step("点击确认购买")
    def click_purchase_btn(self):
        self.purchase_btn.click()

    @allure.step("输入金额并点击申购")
    def purchase(self, amt):
        self.input_amt(amt)
        self.click_purchase_btn()
