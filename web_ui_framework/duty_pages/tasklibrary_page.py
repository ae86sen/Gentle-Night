
import os

import time

from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf


class TasklibraryPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("duty_url","tasklibrary")
    steps_path = os.path.join(os.path.dirname(__file__),"task_libary_page_steps.yaml")

    def open_tasklibrary(self):
        """打开履职管理-任务库页面"""
        return self.driver.get(self.url)

    def add_important_task(self):
        """任务库-添加重要任务"""
        return self.steps(self.steps_path)

    def add_other_task(self):
        """任务库-添加其它任务"""
        return self.steps(self.steps_path)

    def add_spot_task(self):
        """任务库-添加现场任务"""
        return self.steps(self.steps_path)

    def search_important_task(self):
        """搜索添加的重要任务"""
        return self.steps(self.steps_path)

    def search_other_task(self):
        """搜索添加的其它任务"""
        self.driver.refresh()
        return self.steps(self.steps_path)

    def search_spot_task(self):
        """搜索添加的现场任务"""
        return self.steps(self.steps_path)

    def edit_important_task(self):
        """编辑重要任务名称"""
        return self.steps(self.steps_path)

    def edit_other_task(self):
        """编辑其他任务名称"""
        return self.steps(self.steps_path)

    def edit_spot_task(self):
        """编辑现场任务名称"""
        return self.steps(self.steps_path)

    def del_important_task(self):
        """删除重点任务"""
        self.search_important_task()
        n1 = self.get_task_number()
        n2 = self.steps(self.steps_path)[0]
        n3 = self.get_task_number()
        return n1 - n2 == n3

    def del_other_task(self):
        """删除其他任务"""
        self.search_other_task()
        n1 = self.get_task_number()
        n2 = self.steps(self.steps_path)[0]
        n3 = self.get_task_number()
        return n1 - n2 == n3

    def del_spot_task(self):
        """删除现场任务"""
        self.search_spot_task()
        n1 = self.get_task_number()
        n2 = self.steps(self.steps_path)[0]
        n3 = self.get_task_number()
        return n1 - n2 == n3

    def get_task_number(self):
        """获取任务数量"""
        e:str = self.get_element(By.XPATH,"//li[@class='ant-pagination-total-text']").text
        li = e.split(" ")
        return int(li[1])
