
import os
import time
import datetime
import random

from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf

class DutyPlanPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("duty_url","dutyplan")
    steps_path = os.path.join(os.path.dirname(__file__),"duty_plan_steps.yaml")

    def open_dutyplan(self):
        """打开履职管理-值班计划页面"""
        return self.driver.get(self.url)

    def batch_add_plan(self):
        """批量添加值班计划"""
        box_locator = (By.XPATH,"//div[@class='ant-confirm-body-wrapper']")
        box_confirm_locator = (By.XPATH,"//div[@class='ant-confirm-body-wrapper']//button[2]")
        success_logo_locator = (By.XPATH,"//i[@class='anticon anticon-info-circle']/following-sibling::span")
        today = datetime.date.today()
        self._params["start_time"] = str(today + datetime.timedelta(days=1))
        self._params["end_time"] = str(today + datetime.timedelta(days=7))
        self.steps(self.steps_path)
        if self.get_element(box_locator):
            self.wait_element_clickable(box_confirm_locator).click()
            time.sleep(3)
        return self.wait_element_text(success_logo_locator,"批量添加成功")

    def setting(self):
        """设置交接班偏差时间"""
        success_logo_locator = (By.XPATH, "//i[@class='anticon anticon-check-circle']/following-sibling::span")
        self._params['time']= str(random.randint(1,60))
        self.steps(self.steps_path)
        return self.wait_element_text(success_logo_locator,"设置成功")

    def prevent_sleep(self):
        """防瞌睡设置"""
        success_logo_locator = (By.XPATH, "//i[@class='anticon anticon-info-circle']/following-sibling::span")
        self._params['time'] = str(random.randint(1, 10))
        self.steps(self.steps_path)
        return self.wait_element_text(success_logo_locator, "设置成功")

    def prevent_sleep_clear(self):
        """防瞌睡设置还原"""
        self.steps(self.steps_path)

