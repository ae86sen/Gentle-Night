


from common.base_page import BasePage
from common.getconfig import conf
class StandingPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("standingbook_url", "stadingbook")
    def open_standing(self):
        """打开项目台账-项目台账页面"""
        return self.driver.get(self.url)