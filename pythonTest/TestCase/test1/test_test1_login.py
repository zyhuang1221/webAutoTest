from PageCheck.HomePage import *
from PageCheck.User_Login_Page import *
from PageCheck.Merchant_Total_Page import *
from conftest import *


file = get_yaml("./TestFile/test1/login.yaml")


# 给params传入参数化数据,ids传入case名称列表
@pytest.mark.test1
@pytest.fixture(params=file, ids=[data.get('casename') for data in file])
def param_data(request):
    return request.param  # 返回request对象中的param，这里存放的就是参数化数据


@pytest.mark.test1
def test_login(user_driver, param_data):
    print("\n---------------------------------------开始执行用例： "
          + param_data.get('casename') + "----------------------------------------")
    user_driver.get("https://sit-personal.zocaifu.com/")  # 根据环境标识跳转对应首页
    user_driver.delete_all_cookies()  # 清除游览器cookies
    user_driver.refresh()  # 刷新页面
    homePage = HomeWithOutLogin(user_driver)  # 创建首页页面
    homePage.check()  # 检查页面元素
    homePage.click_login()  # 点击登录按钮
    loginPage = LoginPage(user_driver)  # 创建登录页面
    loginPage.check()  # 检查页面元素
    loginPage.login(param_data.get('phoneno'), param_data.get('password'))  # 根据用户名密码登录
    if param_data.get('errormsg') is not None:  # 当用例中errormsg字段不为空时进行错误信息校验
        loginPage.checkPWDError(param_data.get('phoneno'), param_data.get('password'), param_data.get('errormsg'))
    else:
        myAccountPage = MyAccountPage(user_driver)  # 创建我的账户页面
        myAccountPage.checkLoginStatus()  # 校验页面登录状态
