

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.getconfig import conf

class LoginPage(BasePage):

    username_element_locator = (By.XPATH,"//input[@name='Account']")
    pwd_element_locator = (By.XPATH,"//input[@name='password']")

    def login(self,username,pwd):
        # 进入网站
        url = conf.get_str("env","url")
        self.driver.get(url)
        # 定位账号输入框
        username_element = self.get_element(self.username_element_locator)
        # 定位密码输入框
        pwd_element = self.get_element(self.pwd_element_locator)
        # 输入账号密码
        username_element.send_keys(username)
        pwd_element.send_keys(pwd)
        # 点击登录
        pwd_element.submit()

    def login_master(self,username,pwd):
        # 进入网站
        url = conf.get_str("env","url_master")
        self.driver.get(url)
        # 定位账号输入框
        username_element = self.get_element(self.username_element_locator)
        # 定位密码输入框
        pwd_element = self.get_element(self.pwd_element_locator)
        # 输入账号密码
        username_element.send_keys(username)
        pwd_element.send_keys(pwd)
        # 点击登录
        pwd_element.submit()