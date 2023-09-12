import os

import pytest
import allure
from selenium import webdriver
from BaseTools.GetYaml import get_yaml

driver = None


# 注册自定义参数 cmdopt 到配置对象
def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store",
                     default="sit",
                     choices=["test1", "sit"],
                     help="将自定义命令行参数 ’--cmdopt' 添加到 pytest 配置中")


# 从配置对象获取 cmdopt 的值，任何 fixture 或测试用例都可以调用 cmdopt 来获得设备信息
@pytest.fixture(scope='session')
def cmdopt(pytestconfig):
    return pytestconfig.getoption('--cmdopt')


# 配置游览器默认设置
@allure.step("设置游览器配置")
@pytest.fixture(scope="session")
def user_driver():
    # 配置对象
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])  # 禁止浏览器被监控提示
    chromeOptions.add_experimental_option('detach', True)  # 不自动关闭浏览器
    chromeOptions.add_argument('--ignore-certificate-errors')  # 不显示私密链接提示
    # options.add_argument('--headless') # 设置无窗口模式
    # options.add_argument('--disable-gpu') # 禁用gpu加速
    # options.add_argument("--user-agent='  '")  # 设置请求头user-agent
    chromeOptions.add_argument('--start-maximized')  # 设置窗口最大化
    # options.add_argument('--window-size=200,200')  # 设置窗口大小
    chromeOptions.add_argument('--incognito')  # 无痕模式
    # options.add_argument('--hide-scrollbars')  # 隐藏滚动条
    # options.add_argument('--disable-javascript')  # 禁用js
    # options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片（拦截图片）
    # 加载配置
    global driver
    driver = webdriver.Chrome(options=chromeOptions)
    # 前置执行部分
    yield driver
    # 后置执行部分
    print(
        "\n------------------------------------------------用例执行完成--------------------------------------------------")
    driver.quit()


# 获取用例测试结果
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()  # rep可以拿到用例的执行结果详情
    # 以下为实现异常截图的代码：
    # rep.when可选参数有call、setup、teardown，
    # call表示为用例执行环节、setup、teardown为环境初始化和清理环节
    # 这里只针对用例执行且失败的用例进行异常截图
    if rep.when == "call" and rep.failed:
        # 检查driver对象是否包含get_screenshot_as_png方法
        if hasattr(driver, "get_screenshot_as_png"):
            # get_screenshot_as_png实现截图并生成二进制数据
            # allure.attach直接将截图二进制数据附加到allure报告中
            allure.attach(driver.get_screenshot_as_png(), "异常截图", allure.attachment_type.PNG)
