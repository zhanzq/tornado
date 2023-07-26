# encoding=utf-8
# created @2023/07/26
# created by zhanzq
#


import logging


def create_logger(log_path):
    """
    将日志输出到日志文件和控制台
    """
    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')
    # 创建一个handler，用于写入日志文件
    file_handler = logging.FileHandler(filename=log_path, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)

    # 创建一个handler，用于将日志输出到控制台
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    _logger.addHandler(console)

    return _logger


logger = create_logger("./query.log")
