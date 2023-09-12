from PageCheck.Cashier_Purchase_Page import Purchase
from PageCheck.HomePage import *
from PageCheck.Product_List_Page import ProductListPage
from PageCheck.Product_Page import ProductPage
from PageCheck.User_Login_Page import *
from PageCheck.Merchant_Total_Page import *
from conftest import *
from BaseTools.Login import *
from PageCheck.Cashier_Result_Page import *
import logging

# 创建log对象
logger = logging.getLogger(__name__)

# 导入测试用例
file = get_yaml("./TestFile/sit/test_sit_fundPurchase.yaml")


# 给params传入参数化数据,ids传入case名称列表
@pytest.mark.sit
@pytest.fixture(params=file, ids=[data.get('casename') for data in file])
def param_data(request):
    return request.param  # 返回request对象中的param，这里存放的就是参数化数据


@pytest.mark.sit
def test_fund_purchase(user_driver, param_data):
    logger.info("\n---------------------------------------开始执行用例： "
          + param_data.get('casename') + "----------------------------------------")
    user_driver.get("https://sit-personal.zocaifu.com/")  # 根据环境标识跳转对应首页
    login(user_driver, "11042924596", "qwe123")
    merchantpage = MyAccountPage(user_driver)
    merchantpage.click_jxcp()
    productlistpage = ProductListPage(user_driver)
    productlistpage.click_jjzq()
    sleep(5)
    productlistpage.click_first_purchase_btn()
    pruductpage = ProductPage(user_driver)
    pruductpage.purchase('100')
    purchasepage = Purchase(user_driver)
    purchasepage.purchase('滚钱宝', '分红再投', '123123')
    sleep(10)
    assert user_driver.current_url == 'https://sit-cashier.zocaifu.com/cashier/result.htm', "当前不在结果页"
    result = Result(user_driver)
    result.result_assert()

