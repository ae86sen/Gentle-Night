

from common.base_page import BasePage
from common.getconfig import conf
class LocationPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","location")
    def open_location(self):
        """打开安防设备-设备场所页面"""
        return self.driver.get(self.url)