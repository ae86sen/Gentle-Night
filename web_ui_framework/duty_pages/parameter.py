

from common.base_page import BasePage
from common.getconfig import conf
class ParameterPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("duty_url","parameter")
    def open_parameter(self):
        """打开履职管理-参数配置页面"""
        return self.driver.get(self.url)