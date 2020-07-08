

import os

"""
该模块用来整理整个项目目录的路径
"""
#获取项目目录的路径
BASEDIR = os.path.dirname(os.path.dirname(__file__))
#获取配置文件的路径
CONF_DIR = os.path.join(BASEDIR,"conf")
#获取用例数据的路径
DATA_DIR = os.path.join(BASEDIR,"data")
#获取日志文件的路径
LOG_DIR = os.path.join(BASEDIR,"log")
#获取测试报告的路径
REPORT_DIR = os.path.join(BASEDIR,"my_report")
#获取测试用例模块的路径
CASE_DIR = os.path.join(BASEDIR,"test_cases")
#获取上传文件的路径
FILE_DIR = os.path.join(BASEDIR,"upload_files")
ALLURE_DIR = os.path.join(BASEDIR,"alluredir")
print(CONF_DIR)