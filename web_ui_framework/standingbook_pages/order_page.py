

from common.base_page import BasePage
from common.getconfig import conf
class OrderPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("standingbook_url", "order")
    def open_order(self):
        """打开项目台账-项目订购页面"""
        return self.driver.get(self.url)