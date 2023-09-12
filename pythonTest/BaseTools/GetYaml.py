import yaml
import logging

# 创建log对象
logger = logging.getLogger(__name__)


def get_yaml(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as fp:
        f = fp.read()  # 读出来是字符串
    d = yaml.load(f, Loader=yaml.FullLoader)  # 转列表
    logger.info("读取到yaml文件数据")
    logger.info(d)
    return d

