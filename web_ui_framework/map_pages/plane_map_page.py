
import locale
import random

import time

import os
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")

class PlaneMapPage(BasePage):
    """电子地图-平面地图页面"""
    url = conf.get_str("env","url") + conf.get_str("map_url","plane_map")
    # 组织机构展开按键
    org_arrow_btn_locator = (By.XPATH,"//span[@class='ant-select-arrow']")
    # 顶级机构展开按键
    top_org_arrow_locator = (By.XPATH,"//span[@class='ant-select-tree-switcher ant-select-tree-switcher_close']")
    # 第一个下级机构
    first_sub_org_locator = (By.XPATH,"//ul[@class='ant-select-tree-child-tree ant-select-tree-child-tree-open']/li[1]//span[text()]")
    # 当前机构名称
    now_org_name_locator = (By.XPATH,"//span[@class='ant-select-selection-selected-value']/span")
    steps_path = os.path.join(os.path.dirname(__file__), "plane_map_steps.yaml")

    def open_plane_map(self):
        """打开平面地图页面"""
        return self.driver.get(self.url)

    def switch_org(self):
        """切换组织机构"""
        # 点击机构下拉框，然后选择第一个下级机构
        self.get_element(self.org_arrow_btn_locator).click()
        self.get_element(self.top_org_arrow_locator).click()
        self.get_element(self.first_sub_org_locator).click()
        first_sub_org_name = self.get_element(self.first_sub_org_locator).text
        return self.wait_element_text(self.now_org_name_locator,first_sub_org_name)


    def switch_device(self):
        """切换设备"""
        return self.steps(self.steps_path)
