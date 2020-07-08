
from common.base_page import BasePage
from common.getconfig import conf
class WhitePage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("outsiders_url", "whitelist")
    def open_white(self):
        """打开外来人员-白名单页面"""
        return self.driver.get(self.url)