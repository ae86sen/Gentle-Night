

from common.base_page import BasePage
from common.getconfig import conf
class DefencePage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("alarm_url","defence")

    def open_defence(self):
        """打开报警管理-布撤防检测时段页面"""
        return self.driver.get(self.url)
