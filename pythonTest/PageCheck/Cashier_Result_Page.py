import allure
from BaseTools.BasePage import *


# 申购收银台
class Result(BasePage):
    _loc_resulttext = '/html/body/article/article/div/div/p[1]'  # 结果页提示文案

    @allure.step("结果页提示文案")
    def result_text(self):
        logger.info("正在获取文案： result_text")
        self._loc_resulttext.text()
        logger.info("已获取文案： result_text" + self._loc_resulttext.text)

    @allure.step("判断文案是否成功")
    def result_assert(self):
        text = self.result_text()
        logger.info("---------------------------:text" + text)
        assert text == "恭喜您", "交易结果页校验失败"

