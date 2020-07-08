

from common.base_page import BasePage
from common.getconfig import conf
class AuthorizationPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","authorization")
    def open_authorization(self):
        """打开安防设备-黑白名单页面"""
        return self.driver.get(self.url)