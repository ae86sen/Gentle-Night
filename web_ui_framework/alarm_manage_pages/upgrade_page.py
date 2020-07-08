


from common.base_page import BasePage
from common.getconfig import conf
class UpgradePage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("alarm_url","upgrade")

    def open_upgrade(self):
        """打开报警管理-业务报警页面"""
        return self.driver.get(self.url)
