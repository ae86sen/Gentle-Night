


from common.base_page import BasePage
from common.getconfig import conf
class BlackPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("outsiders_url", "blacklist")
    def open_black(self):
        """打开外来人员-黑名单页面"""
        return self.driver.get(self.url)