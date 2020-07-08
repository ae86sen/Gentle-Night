

from common.base_page import BasePage
from common.getconfig import conf
class AlarmPlanPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("alarm_url","alarmplan")

    def open_alarmplan(self):
        """打开报警管理-报警预案页面"""
        return self.driver.get(self.url)
