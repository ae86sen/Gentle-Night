

from common.base_page import BasePage
from common.getconfig import conf
class DefaultPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("alarm_url","default")

    def open_default(self):
        """打开报警管理-常规页面"""
        return self.driver.get(self.url)
