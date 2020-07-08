
import inspect
import json
import logging
import random

import time

import os
import yaml
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from common.wrapper import running_info
class BasePage:
    _params = {}

    def __init__(self,driver):
        self.driver:WebDriver = driver

    @running_info
    def get_element(self,locator, value: str = None):
        if isinstance(locator,tuple):
            element = self.driver.find_element(*locator)
        else:
            element = self.driver.find_element(locator,value)
        return element

    @running_info
    def get_elements(self,locator, value: str = None):
        """获取多个元素"""
        if isinstance(locator, tuple):
            elements = self.driver.find_elements(*locator)
        else:
            elements = self.driver.find_elements(locator, value)
        return elements

    @running_info
    def wait_element_clickable(self, locator,value: str = None, timeout=5, poll_frequency=0.5):
        """等待元素可被点击"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        if isinstance(locator,tuple):
            element = wait.until(EC.element_to_be_clickable(locator))
        else:
            element = wait.until(EC.element_to_be_clickable((locator,value)))
        return element

    def wait_element_precence(self, locator, timeout=5, poll_frequency=0.5):
        """等待元素出现在DOM树中"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_element_visible(self, locator, value:str = None, timeout=5, poll_frequency=0.5):
        """等待元素出现在DOM树中且在页面可见"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        if isinstance(locator, tuple):
            element = wait.until(EC.visibility_of_element_located(locator))
        else:
            element = wait.until(EC.visibility_of_element_located((locator, value)))
        return element


    def wait_element_text(self,locator,text,timeout=5,poll_frequency=0.5):
        """等待某个元素的文本中包含某文字。包含返回TRUE，反之返回FALSE。"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.text_to_be_present_in_element(locator,text_=text))

    def wait_element_not_text(self, locator, text, timeout=5, poll_frequency=0.5):
        """等待某个元素的文本中 不 包含某文字。包含返回TRUE，反之返回FALSE。"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until_not(EC.text_to_be_present_in_element(locator, text_=text))

    def iframe_switch_wait(self):
        """进行iframe切换并等待"""
        wait = WebDriverWait(self.driver, 5, 0.2)
        wait.until(EC.frame_to_be_available_and_switch_to_it(0))

    def alert_switch_wait(self):
        """进行alert弹窗切换并等待"""
        wait = WebDriverWait(self.driver, 5, 0.2)
        alert = wait.until(EC.alert_is_present())
        return alert

    def isElementExist(self,locator):
        """判断一个元素是否存在"""
        try:
            self.get_element(locator)
            return True
        except:
            return False

    def ac_hover(self,elem):
        """鼠标悬停到某个元素上"""
        ac = ActionChains(self.driver)
        ac.move_to_element(elem)
        ac.perform()

    def ac_click(self,elem):
        """鼠标点击某个元素"""
        ac = ActionChains(self.driver)
        ac.click(elem)
        ac.perform()

    def ac_double_click(self,elem):
        """鼠标双击某个元素"""
        ac = ActionChains(self.driver)
        ac.double_click(elem).perform()

    def ac_hover_by_offset_and_click(self, xoffset, yoffset):
        """鼠标悬停到某个坐标上并点击"""
        ac = ActionChains(self.driver)
        ac.move_by_offset(xoffset,yoffset).click().perform()
        # ac.click()

    def random_ip(self):
        """生成随机ip"""
        ip = str(random.randint(1, 256)) + '.' + str(random.randint(1, 256)) + '.' + str(random.randint(1, 256)) + '.' \
             + str(random.randint(1, 253))
        return ip

    def find_file(self,path,name):
        for a, b, c in os.walk(path):
            for file in c:
                if name in file:
                    return True


    def steps(self,path):
        """解析yaml文件中的测试步骤"""
        with open(path,encoding='utf-8') as f:
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps) # 将字典转化成字符串
        if len(self._params) <= 1:
            for key, value in self._params.items():
                # 替换yaml文件中的参数值
                raw = raw.replace("send_value",value)
            steps = json.loads(raw)
        else:
            for key, value in self._params.items():
                # 替换yaml文件中的参数值
                raw = raw.replace("send_value", value,1)
            steps = json.loads(raw)
        rvs = []
        for step in steps:
            if "return_value" in step.keys():
                if "number" in step.keys():
                    # 返回值是数量
                    time.sleep(1)
                    rv = len(self.get_elements(step["by"],step["locator"]))
                    rvs.append(rv)
                elif "value" in step.keys():
                    # 返回值是输入的值
                    rvs.append(step["value"])
                elif "attribute" in step.keys():
                    rv = self.get_element(step["by"],step["locator"]).get_attribute(step["attribute"])
                    rvs.append(rv)
                else:
                    # 返回值是元素文本
                    rv = self.wait_element_visible(step["by"],step["locator"]).text
                    rvs.append(rv)
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    if "wait" in step.keys():
                        if "clickable" == step["wait"]:
                            self.wait_element_clickable(step["by"],step["locator"]).click()
                    else:
                        self.get_element(step["by"], step["locator"]).click()
                elif "send" == action:
                    self.get_element(step["by"], step["locator"]).send_keys(step["value"])
                elif "clear" == action:
                    self.get_element(step["by"], step["locator"]).clear()
                elif "ac_double_click" == action:
                    e = self.get_element(step["by"], step["locator"])
                    self.ac_double_click(e)
                elif "ac_hover" == action:
                    e = self.get_element(step["by"], step["locator"])
                    self.ac_hover(e)
            if "sleep" in step.keys():
                time.sleep(step["sleep"])
        return rvs