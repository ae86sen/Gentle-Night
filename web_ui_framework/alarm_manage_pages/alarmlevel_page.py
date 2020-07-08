
from common.base_page import BasePage
from common.getconfig import conf
class AlarmLevelPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("alarm_url","alarmlevel")

    def open_alarmlevel(self):
        """打开报警管理-报警源级别页面"""
        return self.driver.get(self.url)
