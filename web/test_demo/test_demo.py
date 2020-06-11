"""
============================
Author:古一
Time:2020/6/6
E-mail:369799130@qq.com
============================
"""
import shelve
import time

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class TestDemo:

    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("cookies")
        # db["cookies"]=self.driver.get_cookies()
        cookies = db["cookies"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(5)
        db.close()


