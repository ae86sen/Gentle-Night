
from common.base_page import BasePage
from common.getconfig import conf
class DutyassessPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("duty_url","dutyassess")
    def open_dutyassess(self):
        """打开履职管理-值班考核页面"""
        return self.driver.get(self.url)

