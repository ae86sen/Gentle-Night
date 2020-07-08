

from common.base_page import BasePage
from common.getconfig import conf
class ProductPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("standingbook_url", "productmanage")
    def open_product(self):
        """打开项目台账-产品管理页面"""
        return self.driver.get(self.url)