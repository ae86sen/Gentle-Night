
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
class SeatPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("alarm_url","seatconfig")
    # 组织机构数量
    org_number_locator = (By.XPATH,"//tbody/tr")
    # 展开组织机构树按键
    open_org_btn_locator = (By.XPATH,"//tbody/tr[1]/td/span[contains(@class,'collapsed')]")
    # 添加坐席按键
    add_seat_btn_locator = (By.XPATH,"//tbody/tr[1]/td[2]//a")
    # 删除坐席按键
    del_seat_btn_locator = (By.XPATH,"")
    # 添加坐席箭头按键
    add_seat_arrow_locator = (By.XPATH,"//tbody/tr[1]/td[2]//div[@id='selectSeat']//span")
    # 选择第一个坐席ip
    first_seat_locator = (By.XPATH,"//ul[@role='listbox']/li[1]")
    # 最后一个坐席
    last_seat_locator = (By.XPATH,"//tbody/tr[1]/td[2]/div/div[last()]")
    # 最后一个坐席删除按键
    last_seat_del_locator = (By.XPATH,"//tbody/tr[1]/td[2]/div/div[last()]/i[@class='anticon anticon-cross']")


    def open_seat(self):
        """打开报警管理-接警坐席页面"""
        return self.driver.get(self.url)

    def open_org_tree(self):
        """展开所有组织机构"""
        self.get_element(self.open_org_btn_locator).click()
        return len(self.get_elements(self.org_number_locator)) > 1

    def add_seat(self):
        """添加坐席"""
        # 点击+号添加坐席
        self.get_element(self.add_seat_btn_locator).click()
        # 点击箭头符号展开坐席列表
        self.get_element(self.add_seat_arrow_locator).click()
        # 选择第一个坐席
        seat_elem = self.get_element(self.first_seat_locator)
        seat_elem.click()
        # 新增的坐席
        new_seat_locator = (By.XPATH,"//tbody/tr[1]/td[2]/div/div[text()=' {}']".format(seat_elem.text))
        return self.isElementExist(new_seat_locator)

    def del_seat(self):
        """删除最后一个坐席"""
        last_seat_name = self.get_element(self.last_seat_locator).text
        self.get_element(self.last_seat_del_locator).click()
        del_seat_locator = (By.XPATH,"//tbody/tr[1]/td[2]/div/div[text()=' {}']".format(last_seat_name))
        return self.isElementExist(del_seat_locator)





