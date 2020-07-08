

from common.base_page import BasePage
from common.getconfig import conf
class DeviceBookPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("standingbook_url", "devicebook")
    def open_devicebook(self):
        """打开项目台账-设备台账页面"""
        return self.driver.get(self.url)