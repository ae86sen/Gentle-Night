


from common.base_page import BasePage
from common.getconfig import conf
class ParamPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("basicdata_url", "param")
    def open_param(self):
        """打开参数管理页面"""
        return self.driver.get(self.url)