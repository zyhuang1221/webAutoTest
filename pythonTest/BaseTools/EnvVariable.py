import pytest

from BaseTools.GetYaml import get_yaml


@pytest.fixture(scope="session")
def get_url(cmdopt):
    """解析URL"""
    global url
    if cmdopt == "test1":
        print("当前环境为test1环境")
        url = 'http://test1-personal.zocaifu.com/'
    elif cmdopt == "sit":
        print("当前环境为sit环境")
        url = 'http://sit-personal.zocaifu.com/'
    return url


# 根据环境获取文件地址
@pytest.fixture(scope="session")
def get_test_file(cmdopt):
    global fileURL
    if cmdopt == "test1":
        fileURL = "./TestFile/test1/"
    elif cmdopt == "sit":
        fileURL = "./TestFile/sit/"
    return fileURL



