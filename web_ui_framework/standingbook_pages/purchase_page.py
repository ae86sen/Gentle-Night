

from common.base_page import BasePage
from common.getconfig import conf
class PurchasePage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("standingbook_url", "purchase")
    def open_purchase(self):
        """打开项目台账-项目采购页面"""
        return self.driver.get(self.url)