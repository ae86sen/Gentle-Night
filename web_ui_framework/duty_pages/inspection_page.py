
import os

import datetime
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf

class InspectionPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("duty_url","inspection")
    steps_path = os.path.join(os.path.dirname(__file__),"inspection_steps.yaml")

    def open_inspection(self):
        """打开履职管理-非现场检查页面"""
        return self.driver.get(self.url)

    def check_type(self):
        """检查类型下拉框"""
        arrow_locator = (By.XPATH,"//div[@class='cms-Duty-searchItem'][1]//span[@class='ant-select-arrow']")
        options_locator = (By.XPATH,"//ul[contains(@class,'dropdown-menu-vertical')]/li")
        self.get_element(arrow_locator).click()
        time.sleep(0.1)
        options = self.get_elements(options_locator)
        results = [i.text for i in options]
        return results

    def check_status(self):
        """检查状态下拉框"""
        arrow_locator = (By.XPATH,"//div[@class='cms-Duty-searchItem'][2]//span[@class='ant-select-arrow']")
        options_locator = (By.XPATH, "//ul[contains(@class,'dropdown-menu-vertical')]/li")
        self.get_element(arrow_locator).click()
        time.sleep(0.1)
        options = self.get_elements(options_locator)
        results = [i.text for i in options]
        return results

    def add_important_task(self):
        """添加重要任务"""
        t1 = datetime.datetime.now() + datetime.timedelta(hours=2)
        t2 = datetime.datetime.now() + datetime.timedelta(hours=4)
        self._params["start_time"] = t1.strftime('%Y-%m-%d %H:%M')
        self._params["end_time"] = t2.strftime('%Y-%m-%d %H:%M')
        return self.steps(self.steps_path)

    def add_other_task(self):
        """添加其它任务"""
        t1 = datetime.datetime.now() + datetime.timedelta(hours=2)
        t2 = datetime.datetime.now() + datetime.timedelta(hours=4)
        self._params["start_time"] = t1.strftime('%Y-%m-%d %H:%M')
        self._params["end_time"] = t2.strftime('%Y-%m-%d %H:%M')
        return self.steps(self.steps_path)

    def search_by_name(self):
        """通过名称搜索"""
        today = datetime.datetime.today()
        self._params["time"] = today.strftime('%Y-%m-%d')
        return self.steps(self.steps_path)

    def search_by_worker(self):
        """通过执行人搜索"""
        input_locator = (By.XPATH,"//div[@class='cms-Duty-searchItem'][4]//input")
        worker_name_locator = (By.XPATH,"//tbody/tr[1]//td[6]")
        search_locator = (By.XPATH,"//i[contains(@class,'ant-input')]")
        worker : str = self.wait_element_visible(worker_name_locator).text
        worker_name = worker.split('，')[-1]
        self.get_element(input_locator).send_keys(worker_name)
        time.sleep(0.5)
        self.get_element(search_locator).click()
        time.sleep(0.5)
        new_worker = self.wait_element_visible((By.XPATH,"//tbody/tr[last()]//td[6]")).text
        return worker == new_worker

    def search_by_content(self):
        """通过执行人搜索"""
        input_locator = (By.XPATH,"//div[@class='cms-Duty-searchItem'][4]//input")
        content_locator = (By.XPATH,"//tbody/tr[1]//td[8]")
        search_locator = (By.XPATH,"//i[contains(@class,'ant-input')]")
        content = self.wait_element_visible(content_locator).text
        self.get_element(input_locator).send_keys(content)
        time.sleep(0.5)
        self.get_element(search_locator).click()
        time.sleep(0.5)
        new_content = self.wait_element_visible((By.XPATH,"//tbody/tr[last()]//td[8]")).text
        return content == new_content

    def batch_add_important_task(self,loc):
        """批量添加重点任务"""
        self._params["locator"] = loc
        success_logo_locator = (By.XPATH,"//i[@class='anticon anticon-check-circle']/following-sibling::span")
        self.steps(self.steps_path)
        time.sleep(1)
        return self.wait_element_text(success_logo_locator,"添加成功")

    def batch_add_other_task(self,loc):
        """批量添加其他任务"""
        self._params["locator"] = loc
        success_logo_locator = (By.XPATH, "//i[@class='anticon anticon-check-circle']/following-sibling::span")
        self.steps(self.steps_path)
        time.sleep(1)
        return self.wait_element_text(success_logo_locator, "添加成功")

