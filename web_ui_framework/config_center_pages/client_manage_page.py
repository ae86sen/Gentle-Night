
import locale

import os

from common.base_page import BasePage
from common.getconfig import conf
from common.constants import BASEDIR
steps_path = os.path.join(os.path.dirname(__file__),"client_manage_page.yaml")

class ClientManagePage(BasePage):
    """防范平台-客户端管理页面"""
    url = conf.get_str("env", "url") + conf.get_str("config_center_url", "client_manage")

    def open_client_manage(self):
        """打开防范平台-客户端管理页面"""
        return self.driver.get(self.url)

    def set_normal_time(self,time):
        """设置无操作自动退出时间：1分钟和90分钟"""
        self._params["time"] = time
        return self.steps(steps_path)

    def set_less_boundary_time(self):
        """设置无操作自动退出时间为0"""
        return self.steps(steps_path)

    def set_greater_boundary_time(self):
        """设置无操作自动退出时间为91"""
        return self.steps(steps_path)