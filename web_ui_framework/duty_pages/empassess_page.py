

from common.base_page import BasePage
from common.getconfig import conf
class EmpassessPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("duty_url","employeeassess")
    def open_empassess(self):
        """打开履职管理-员工考核页面"""
        return self.driver.get(self.url)