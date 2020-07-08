
from common.base_page import BasePage
from common.getconfig import conf
import os
class ContentPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("duty_url","content")
    steps_path = os.path.join(os.path.dirname(__file__),"content_page_steps.yaml")
    def open_content(self):
        """打开履职管理-检查内容页面"""
        return self.driver.get(self.url)

    def add_content(self,data):
        """添加内容"""
        self._params["data"] = data
        return self.steps(self.steps_path)

    def add_content_none(self):
        """添加内容为空"""
        return self.steps(self.steps_path)

    def copy_content(self):
        """复制内容"""
        return self.steps(self.steps_path)

    def del_content(self):
        """删除内容"""
        return self.steps(self.steps_path)