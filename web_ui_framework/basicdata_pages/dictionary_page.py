

from common.base_page import BasePage
from common.getconfig import conf
class DictionaryPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("basicdata_url", "dictionary")

    def open_dictionary(self):
        """打开数据字典页面"""
        return self.driver.get(self.url)