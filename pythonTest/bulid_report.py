import os

import pytest

if __name__ == '__main__':
    # pytest.main(['-s', '-v', '--clean-alluredir', '--alluredir=./Report/.allure_results'])
    # pytest.main(['-v', '-s', 'test_test1.py'])
    # pytest.main(['-s', '-v', '-k', 'test_test1.py', '--clean-alluredir', '--alluredir=./Report/.allure_results'])
    pytest.main(['-s', '-v', './TestCase/sit/test_sit_fundPurchase.py', '--clean-alluredir', '--alluredir=./Report/.allure_results'])  # 单独运行指定用例
    # pytest.main(['-m sit', '-s'])  # 运行所有对应标签的用例
    os.system("allure generate ./Report/.allure_results -o ./Report/.html_report --clean")  # 生成html报告


