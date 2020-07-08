
import os

import datetime

import re
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
class DutytaskPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("duty_url","dutytask")
    steps_path = os.path.join(os.path.dirname(__file__),"duty_task_steps.yaml")

    def open_dutytask(self):
        """打开履职管理-值班任务页面"""
        return self.driver.get(self.url)

    def add_duty_task(self):
        """添加值班任务"""
        today = datetime.date.today()
        self._params["start_time"] = str(today + datetime.timedelta(days=1))
        self._params["end_time"] = str(today + datetime.timedelta(days=7))
        results = self.steps(self.steps_path)
        rd = '(\d)'
        li = []
        for i in results:
            res = re.search(rd,i)
            li.append(int(res.group(1)))
        return li

    def check_result(self):
        """查看执行情况"""
        today = datetime.date.today()
        self._params["start_time"] = str(today - datetime.timedelta(days=1))
        self._params["end_time"] = str(today)
        self.steps(self.steps_path)
        locator = (By.XPATH,"//div[@class='pageBreadcrumb']")
        return self.wait_element_text(locator,"非现场检查执行情况")


