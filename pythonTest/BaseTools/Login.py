from PageCheck.HomePage import *
from PageCheck.User_Login_Page import *


@allure.step("默认登录")
def login(driver: webdriver.Chrome, phoneno, password):
    driver.delete_all_cookies()  # 清除游览器cookies
    driver.refresh()  # 刷新页面
    homePage = HomeWithOutLogin(driver)  # 创建首页页面
    homePage.click_login()  # 点击登录按钮
    loginPage = LoginPage(driver)  # 创建登录页面
    loginPage.login(phoneno, password)
