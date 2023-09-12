from BaseTools.BasePage import *
import allure


class LoginPage(BasePage):
    _loc_phoneText = '//*[@id="loginPhone"]'  # 手机号输入框
    _loc_passWordText = '//input[@type="password"]'  # 密码输入框
    _loc_agreeOnTickBox = '//*[@id="check_Login"]'  # 同意协议勾选框
    _loc_loginbtn = '//*[@id="login"]/div[1]/div[1]/div[6]'  # 登录按钮
    _loc_toplogonbtn = '/html/body/div[1]/div/div/div[2]/a'  # 顶部“去注册”按钮
    _loc_downlogonbtn = '//*[@id="login"]/div[1]/div[2]/a'  # “新用户注册”按钮
    _loc_forgetPassWord = '//*[@id="login"]/div[1]/div[1]/div[3]/div[3]/a'  # “忘记登录密码？”按钮
    _loc_resetPassWord = '//*[@id="login-desc"]/div/ul/li[2]/div/a'  # “初始化密码”按钮
    _loc_errormsg = '//*[@id="login"]/div[1]/div[1]/div[3]/div[2]'  # 密码输入框下方报错提示
    _loc_errormsg2 = '//*[@id="login"]/div[1]/div[1]/div[2]/div[2]'  # 手机号输入框下方错误提示

    @allure.step("检查页面元素是否存在")
    def check(self):
        self.phoneText
        self.passWordText
        self.agreeOnTickBox
        self.loginbtn
        self.toplogonbtn
        self.downlogonbtn
        self.forgetPassWord
        self.resetPassWord

    @allure.step("根据输入用户名密码登录")
    def login(self, name, password):
        if name is not None:
            self.phoneText.send_keys(name)
            logger.info("已输入文本： phoneText")
        if password is not None:
            self.passWordText.send_keys(password)
            logger.info("已输入文本： passWordText")
        self.agreeOnTickBox.click()
        logger.info("已点击按钮： agreeOnTickBox")
        self.loginbtn.click()
        logger.info("已点击按钮： loginbtn")

    # 获取错误信息
    @allure.step("获取错误信息")
    def __getErrorMsg(self):
        logger.info("获取错误信息： " + self.errormsg.text)
        return self.errormsg.text

    # 比对错误信息
    @allure.step("比对错误信息")
    def checkPWDError(self, phoneno, password, errorMsg):
        sleep(1)
        if phoneno is None:
            logger.info(self.errormsg2.text)
            assert errorMsg == self.errormsg2.text
        elif password is None:
            logger.info(self.errormsg.text)
            assert errorMsg == self.errormsg.text
        else:
            logger.info(self.errormsg.text)
            assert errorMsg == self.errormsg.text

