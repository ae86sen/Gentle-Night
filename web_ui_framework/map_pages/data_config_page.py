
import locale

import os
import pyautogui as ui
import time
from selenium.webdriver.common.by import By
from common.constants import FILE_DIR
from common.base_page import BasePage
from common.getconfig import conf

class DataConfigPage(BasePage):
    """电子地图-数据配置页面"""
    url = conf.get_str("env","url") + conf.get_str("map_url","base")

    def open_data_config(self):
        """打开数据配置页面"""
        return self.driver.get(self.url)

    def upload_gis(self):
        """上传gis包"""
        upload_btn_locator = (By.XPATH,"//input[@type='file']")
        self.wait_element_clickable(upload_btn_locator).click()
        # 文件导入地址
        time.sleep(1)
        file_path = os.path.join(FILE_DIR,"gis_7_12.rar")
        ui.write(file_path)
        time.sleep(2)
        ui.press("enter", 2)
        time.sleep(1)


    def init_org(self):
        """初始化组织机构"""
        init_btn_locator = (By.ID,"btnSyncOrgInfo")
        self.wait_element_clickable(init_btn_locator).click()
        time.sleep(1800)


    def config_xm_service(self):
        """配置讯美地图服务"""
        map_select_locator = (By.CSS_SELECTOR,"#MapEngineType")
        xm_option_locator = (By.XPATH,"//select/option[2]")
        save_btn_locator = (By.ID,"SaveServer")
        save_success_locator = (By.XPATH,"//div[@class='bootbox-body']")
        self.iframe_switch_wait()
        # self.get_element(map_select_locator).click()
        self.get_element(xm_option_locator).click()
        self.get_element(save_btn_locator).click()
        return self.wait_element_text(save_success_locator,"保存成功")