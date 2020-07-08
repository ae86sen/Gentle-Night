

from common.base_page import BasePage
from common.getconfig import conf
class OutsiderPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("outsiders_url", "outsider")
    def open_outsider(self):
        """打开外来人员-外来人员页面"""
        return self.driver.get(self.url)