

from common.base_page import BasePage
from common.getconfig import conf
class ProjectPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("standingbook_url", "project")
    def open_project(self):
        """打开项目台账-项目页面"""
        return self.driver.get(self.url)