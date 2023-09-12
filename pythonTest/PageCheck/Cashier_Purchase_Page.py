import allure

from BaseTools.BasePage import *


# 申购收银台
class Purchase(BasePage):
    _loc_purchase_password = '//*[@id="payPassword"]'  # 交易密码输入栏
    _loc_xjfh = '//*[@id="frm"]/div[2]/span[2]'  # 现金分红
    _loc_fhzt = '//*[@id="frm"]/div[2]/span[3]'  # 分红再投
    _loc_gqb = '//*[@id="tab_typeNameGqb"]'  # 滚钱宝支付工具
    _loc_yhk = '//*[@id="frm"]/div[1]/div[1]/label'  # 银行卡支付工具
    _loc_comfirm_btn = '//*[@id="confirmBtn"]'  # 确认按钮
    _loc_resume_comfirm_btn = '//*[@id="productFileModal"]/div/div/div[2]/div/div[2]/a[2]'  # 确认基金产品概要

    # 点击滚钱宝支付工具
    @allure.step("点击滚钱宝支付工具")
    def click_gqb(self):
        self.gqb.click()
        logger.info("已点击按钮： gqb")

    @allure.step("点击银行卡支付工具")
    def click_yhk(self):
        self.yhk.click()
        logger.info("已点击按钮： yhk")

    @allure.step("点击现金分红")
    def click_xjfh(self):
        self.xjfh.click()
        logger.info("已点击按钮： xjfh")

    @allure.step("点击分红再投")
    def click_fhzt(self):
        self.fhzt.click()
        logger.info("已点击按钮： fhzt")

    @allure.step("输入密码")
    def input_password(self, password):
        self.purchase_password.send_keys(password)
        logger.info("已输入密码： purchase_password")

    @allure.step("点击确认按钮")
    def click_comfirm_btn(self):
        self.comfirm_btn.click()
        logger.info("已点击按钮： comfirm_btn")

    # 基金申购
    @allure.step("基金申购")
    def purchase(self, paytool, bonus, password):
        if paytool == '滚钱宝':
            logger.info('寻找滚钱宝支付工具')
            self.click_gqb()
        elif paytool == '银行卡':
            self.click_yhk()
        else:
            assert False, "输入支付工具不匹配"
        if bonus == '现金分红':
            self.click_xjfh()
        elif bonus == '分红再投':
            self.click_fhzt()
        else:
            assert False, "输入分红方式不匹配"
        self.input_password(password)
        self.click_comfirm_btn()


