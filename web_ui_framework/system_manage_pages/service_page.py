
import os

import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
class ServicePage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("system_manage_url","service")
    # 添加服务器按键
    add_server_btn_locator = (By.XPATH,"//button[@id='add']")
    # 第一个服务器的下载代理按键
    download_agent_btn_locator = (By.XPATH,"//div[@id='serverList']/div[1]//button[@id='downLoad']")

    def open_service(self):
        """打开履职管理-检查内容页面"""
        return self.driver.get(self.url)

    def download_agent(self):
        """下载网络代理"""
        # 检查系统中有无代理文件，有就删除
        for a, b, c in os.walk(r"C:\Users"):
            for file in c:
                if "Agent_192.168." in file:
                    os.remove(os.path.join(a, file))
        # 添加服务器
        self.wait_element_clickable(self.add_server_btn_locator).click()
        # 点击下载代理
        self.get_element(self.download_agent_btn_locator).click()
        time.sleep(5)
        # 检查系统中有无新下载的代理文件
        for a, b, c in os.walk(r"C:\Users"):
            for file in c:
                if "Agent_192.168." in file:
                    os.remove(os.path.join(a, file))
                    return True
