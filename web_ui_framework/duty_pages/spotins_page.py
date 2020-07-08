

from common.base_page import BasePage
from selenium.webdriver.common.by import By
from common.getconfig import conf
import datetime
import time
import os
from selenium.webdriver import ActionChains


class SpotinsPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("duty_url", "spotinspection")
    steps_path = os.path.join(os.path.dirname(__file__), "spotins_steps.yaml")

    def open_spotinspection(self):
        """打开履职管理-现场检查页面"""
        return self.driver.get(self.url)

    def check_state_contents(self):
        "检查状态下拉框"
        arrow_locator = (By.XPATH, "//div[@class='cms-Duty-searchItem'][1]//span[@class='ant-select-arrow']")
        options_locator = (By.XPATH, "//ul[contains(@class,'ant-select-dropdown-menu')]//li")

        self.get_element(arrow_locator).click()
        options = self.get_elements(options_locator)
        time.sleep(0.2)
        results = [i.text for i in options]
        return results

    def check_add_task(self, name):
        '''添加现场任务'''
        t1 = datetime.datetime.now() + datetime.timedelta(hours=2)
        t2 = datetime.datetime.now() + datetime.timedelta(hours=4)
        self._params["start_time"] = t1.strftime('%Y-%m-%d %H:%M')
        self._params["end_time"] = t2.strftime('%Y-%m-%d %H:%M')
        return self.steps(self.steps_path)

    def selct_by_name(self, name):
        '''按名称搜索'''
        t1 = datetime.datetime.now()
        self._params["start_time"] = t1.strftime('%Y-%m-%d')
        self._params["end_time"] = t1.strftime('%Y-%m-%d')
        self._params["name"] = name
        return self.steps(self.steps_path)

    # def selct_by_person(self, person):
    #     '''按执行人搜索'''
    #     t1 = datetime.datetime.now()
    #     self._params["start_time"] = t1.strftime('%Y-%m-%d')
    #     self._params["end_time"] = t1.strftime('%Y-%m-%d')
    #     self._params["person"] = person
    #     print("执行人",person)
    #     return self.steps(self.steps_path)
    #
    # def selct_by_content(self, content):
    #     '''按内容搜索'''
    #     t1 = datetime.datetime.now()
    #     # self._params["start_time"] = t1.strftime('%Y-%m-%d')
    #     # self._params["end_time"] = t1.strftime('%Y-%m-%d')
    #     self._params["start_time"] = "2020-05-22"
    #     self._params["end_time"] = "2020-05-25"
    #     self._params["person"] = content
    #     print("内容", content)
    #     return self.steps(self.steps_path)

    # def check_add_task(self, name):
    #     '''添加现场任务'''
    #     # 添加按钮
    #     add_locator = (By.XPATH, "//button[contains(@class,'cms-marginRight-xs')]")
    #     # 任务名称
    #     name_locator = (By.ID, 'name')
    #     # 点击开始时间
    #     start_time_locator = (By.XPATH, "//span[@id='startTime']//input")
    #     # 开始时间输入框
    #     start_time_input_locator = (By.XPATH, "//input[@class='ant-calendar-input ']")
    #     # 确定按钮
    #     start_time_input_ok_locator = (By.XPATH, "//a[@class='ant-calendar-ok-btn']")
    #     # 结束
    #     end_time_locator = (By.XPATH, "//span[@id='endTime']//input")
    #     # 结束时间输入
    #     end_time_input_locator = (By.XPATH, "//input[@class='ant-calendar-input ']")
    #     # 结束确定
    #     end_time_input_ok_locator = (By.XPATH, "//a[@class='ant-calendar-ok-btn']")
    #     # 添加人员按钮
    #     duty_person_button_locator = (By.XPATH, "//div[@id='UserSelect']/button")
    #     # 勾选人员1
    #     duty_person_add_1_locator = (By.XPATH, "//div[@id='UserSelectTable']//tbody/tr[1]//input")
    #     # 勾选人员2
    #     duty_person_add_2_locator = (By.XPATH, "//div[@id='UserSelectTable']//tbody/tr[2]//input")
    #     duty_person_ok_locator = (By.XPATH, "//div[contains(@style,'width: 1200px')]//span[text()='确 定']/parent::button")
    #     # 组织机构按钮
    #     organ_button_locator = (By.XPATH, "//span[@class='ant-select-search__field__placeholder']")
    #     # 展开组织机构
    #     organ_show_locator = (By.XPATH, "//span[contains(@class,'ant-select-tree-node-content-wrapper-close')]")
    #     arrow_locator = (By.XPATH,"//ul[ @class ='ant-select-tree']/li/span[1]")
    #     #"//ul[@class='ant-select-tree']//span[contains(@class,'tree-switcher_close')]"
    #     # 选择组织机构1
    #     organ_select_locator = (By.XPATH, "//ul[@class='ant-select-tree']//li[1]//span[contains(@class,'content-wrapper-open')]")
    #     # 选择组织机构2
    #     organ_select_1_locator = (By.XPATH, "//ul[contains(@class,'ant-select-tree-child-tree')]//span[2]")
    #     # 空白区域
    #     blank_area_locator = (By.XPATH, "//ul[@class='ant-select-selection__rendered']")
    #     # 受检区域
    #     area_button_locator = (By.XPATH, "//div[@class='ant-dropdown-trigger']")
    #     # 受检区域勾选
    #     area_select_locator = (By.XPATH, "//div[contains(@style,'min-width: 320px')]//li[2]//input")
    #     # 从任务库中选择
    #     task_store_locator = (By.LINK_TEXT,"从任务库选择")
    #     # 备注
    #     ramark_locator = (By.ID, "remark")
    #     # 保存按钮
    #     save_button = (By.XPATH, "//div[contains(@style,'width: 600px')]//span[text()='确 定']/parent::button")
    #     # 新增任务名称
    #     get_task_name = (By.XPATH, "//tbody/tr[1]//a")
    #     t1 = datetime.datetime.now() + datetime.timedelta(hours=2)
    #     t2 = datetime.datetime.now() + datetime.timedelta(hours=4)
    #     start_time = t1.strftime('%Y-%m-%d %H:%M')
    #     end_time = t2.strftime('%Y-%m-%d %H:%M')
    #
    #     #点击添加按钮
    #     self.get_element(add_locator).click()
    #     #输入任务名称
    #     self.get_element(name_locator).send_keys(name)
    #     #开始时间输入
    #     self.get_element(start_time_locator).click()
    #     time.sleep(0.2)
    #     self.get_element(start_time_input_locator).send_keys(start_time)
    #     self.get_element(start_time_input_ok_locator).click()
    #     #结束时间输入
    #     self.get_element(end_time_locator).click()
    #     time.sleep(0.2)
    #     self.get_element(end_time_input_locator).send_keys(end_time)
    #     self.get_element(end_time_input_ok_locator).click()
    #     time.sleep(0.2)
    #     #添加执行人
    #     self.get_element(duty_person_button_locator).click()
    #     time.sleep(0.2)
    #     self.get_element(duty_person_add_1_locator).click()
    #     time.sleep(0.2)
    #     self.get_element(duty_person_add_2_locator).click()
    #     self.get_element(duty_person_ok_locator).click()
    #     #组织机构
    #     time.sleep(0.2)
    #     self.get_element(organ_button_locator).click()
    #     time.sleep(0.2)
    #     #点击箭头展开机构
    #     self.get_element(arrow_locator).click()
    #     time.sleep(0.5)
    #     #选择两个组织机构
    #     self.get_element(organ_select_locator).click()
    #     self.get_element(organ_select_1_locator).click()
    #     time.sleep(0.5)
    #     #点击其他区域关闭弹窗
    #     self.get_element(blank_area_locator).click()
    #     #鼠标悬浮选择区域
    #     ele = self.get_element(area_button_locator)
    #     self.ac_hover(ele)
    #     self.get_element(area_select_locator).click()
    #     #输入备注
    #     self.get_element(ramark_locator).send_keys("备注备注备注备注备注备注备注备注备注备注备注备注备注备备注备注备注备注备注备注备注备注备注备注备注备注备注备备注备注备注备注备注备注备注备注备注备注备注备注备注备备注备注备注备注备注备注备注备注备注备注备注备注备注备备注备注备注备注备注备注备注备注备注备注备注备注备注备备注备注备注备注备注备注备注备注备注备注备注备注备注备备注备注备注备注备注备注备注备注备注备注备注备注备注备备注备注备注备注备注备11111")
    #     #点击确定按钮保存
    #     self.get_element(save_button).click()
    #     time.sleep(1)
    #     #获取新增任务的任务名
    #     result = self.get_element(get_task_name).text
    #     print(result)
    #     return result

    # def selct_by_name(self, name):
    #     '''按名称搜索'''
    #     #清除时间
    #     clear_time_locator = (By.XPATH, "//span[contains(@class,'ant-calendar-picker-icon')]")
    #     #时间控件
    #     time_locator = (By.XPATH, "//span[contains(@class,'ant-calendar-picker-input ant-input')]")
    #     #开始时间输入框
    #     start_time_locator = (By.XPATH, "//div[contains(@class,'range-left')]//input[1]")
    #     #结束时间输入框
    #     end_time_locator = (By.XPATH, "//div[contains(@class,'range-right')]//input[1]")
    #     #名称输入框
    #     input_locator = (By.XPATH, "//span[contains(@class,'wrapper')]/input")
    #     # 查询按钮
    #     search_button = (By.XPATH, "//span[contains(@class,'wrapper')]/../button")
    #     # 获取查询出的所有任务名称tr
    #     tr_locator = (By.TAG_NAME, "tr")
    #
    #
    #     time.sleep(0.5)
    #     #清除时间框
    #     self.get_element(clear_time_locator).click()
    #     #点击时间控件
    #     self.get_element(time_locator).click()
    #     time.sleep(0.5)
    #     #设置当前日期并定义格式
    #     t1 = datetime.datetime.now()
    #     times = t1.strftime('%Y-%m-%d')
    #     #传值至时间输入框中
    #     self.get_element(start_time_locator).send_keys(times)
    #     self.get_element(end_time_locator).send_keys(times)
    #     #传值至名称输入框中
    #     self.get_element(input_locator).send_keys(name)
    #     #点击查询按钮
    #     self.get_element(search_button).click()
    #     time.sleep(0.5)
    #     #查询表格最后一条数据
    #     row = self.get_elements(tr_locator)
    #     lenth = len(row)
    #     last = row[lenth - 1].text
    #     last_list = last.split(" ")
    #     print(last_list[1])
    #     return last_list[1]

    # def selct_by_person(self, person):
    #     '''按执行人搜索'''
    #     #清除时间
    #     clear_time_locator = (By.XPATH, "//span[contains(@class,'ant-calendar-picker-icon')]")
    #     #时间控件
    #     time_locator = (By.XPATH, "//span[contains(@class,'ant-calendar-picker-input ant-input')]")
    #     #开始时间输入框
    #     start_time_locator = (By.XPATH, "//div[contains(@class,'range-left')]//input[1]")
    #     #结束时间输入框
    #     end_time_locator = (By.XPATH, "//div[contains(@class,'range-right')]//input[1]")
    #     #名称输入框
    #     input_locator = (By.XPATH, "//span[contains(@class,'wrapper')]/input")
    #     # 查询按钮
    #     search_button = (By.XPATH, "//span[contains(@class,'wrapper')]/../button")
    #     # tr
    #     tr_locator = (By.TAG_NAME, "tr")
    #     time.sleep(0.5)
    #     self.get_element(clear_time_locator).click()
    #     #点击时间控件
    #     self.get_element(time_locator).click()
    #     time.sleep(0.5)
    #     #设置当前日期并定义格式
    #     t1 = datetime.datetime.now()
    #     times = t1.strftime('%Y-%m-%d')
    #     #传值至时间输入框中
    #     self.get_element(start_time_locator).send_keys(times)
    #     self.get_element(end_time_locator).send_keys(times)
    #     #传值至名称输入框中
    #     self.get_element(input_locator).send_keys(person)
    #     #点击查询按钮
    #     self.get_element(search_button).click()
    #     time.sleep(0.5)
    #     #查询表格最后一条数据
    #     row = self.get_elements(tr_locator)
    #     lenth = len(row)
    #     last = row[lenth - 1].text
    #     last_list = last.split(" ")
    #     print(last_list[8])
    #     return last_list[8]


    # def selct_by_content(self, content):
    #     '''按内容搜索'''
    #     #清除时间
    #     clear_time_locator = (By.XPATH, "//span[contains(@class,'ant-calendar-picker-icon')]")
    #     #时间控件
    #     time_locator = (By.XPATH, "//span[contains(@class,'ant-calendar-picker-input ant-input')]")
    #     #开始时间输入框
    #     start_time_locator = (By.XPATH, "//div[contains(@class,'range-left')]//input[1]")
    #     #结束时间输入框
    #     end_time_locator = (By.XPATH, "//div[contains(@class,'range-right')]//input[1]")
    #     #名称输入框
    #     input_locator = (By.XPATH, "//span[contains(@class,'wrapper')]/input")
    #     # 查询按钮
    #     search_button = (By.XPATH, "//span[contains(@class,'wrapper')]/../button")
    #     # tr
    #     tr_locator = (By.TAG_NAME, "tr")
    #     time.sleep(0.5)
    #     self.get_element(clear_time_locator).click()
    #     #点击时间控件
    #     self.get_element(time_locator).click()
    #     time.sleep(0.5)
    #     #设置当前日期并定义格式
    #     t1 = datetime.datetime.now()
    #     times = t1.strftime('%Y-%m-%d')
    #     #传值至时间输入框中
    #     self.get_element(start_time_locator).send_keys(times)
    #     self.get_element(end_time_locator).send_keys(times)
    #     #传值至名称输入框中
    #     self.get_element(input_locator).send_keys(content)
    #     #点击查询按钮
    #     self.get_element(search_button).click()
    #     time.sleep(0.5)
    #     #查询表格最后一条数据
    #     row = self.get_elements(tr_locator)
    #     lenth = len(row)
    #     last = row[lenth - 1].text
    #     last_list = last.split(" ")
    #     print(last_list[9])
    #     return last_list[9]

    def check_details_button(self):
        '''查看执行情况详情'''
        details_location = (By.XPATH, "//tr[contains(@class,' cms-table-isSelected')]/td[11]/div/a")
        title_location = (By.XPATH, "//div[@class='pageBreadcrumb']")

        self.get_element(details_location).click()
        time.sleep(1)
        title = self.get_element(title_location).text
        return title

    def check_delete_unexecuted(self):
        '''删除未执行的任务'''
        #点击状态下拉框
        row_locator = (By.XPATH, "//div[@class='cms-Duty-searchItem'][1]//span[@class='ant-select-arrow']")
        #点击状态为 未到执行时间的
        state_locator = (By.XPATH, "//ul[contains(@class,'ant-select-dropdown-menu')]//li[2]")
        # 查询按钮
        search_button = (By.XPATH, "//span[contains(@class,'wrapper')]/../button")
        # 勾选数据名称
        name_locator = (By.XPATH, "//tr[contains(@class,' cms-table-isSelected')]/td[3]//a")
        # 勾选一条数据
        checkBox_locator = (By.XPATH, "//tr[contains(@class,' cms-table-isSelected')]/td[1]//input")
        #删除按钮
        delete_button = (By.XPATH, "//div[@class='ant-col-6']/button")
        #确定按钮
        ok_button = (By.XPATH, "//div[@class='ant-popover-buttons']/button[2]")
        #删除成功弹出图标
        delete_text = (By.XPATH, "//i[@class='anticon anticon-check-circle']/following-sibling::span")

        # 点击状态下拉框
        self.get_element(row_locator).click()
        # 点击状态为 未到执行时间的
        self.get_element(state_locator).click()
        # 查询按钮
        self.get_element(search_button).click()
        #获取删除的任务名称
        task_name = self.get_element(name_locator).text
        #勾选一条数据
        self.get_element(checkBox_locator).click()
        #删除按钮
        self.get_element(delete_button).click()
        time.sleep(0.54)
        #确定按钮
        self.get_element(ok_button).click()
        #删除成功弹出图标
        text_result = self.wait_element_text(delete_text, "删除成功")
        print(text_result)
        name = self.selct_by_name(task_name)
        print("ss")
        print(type(name))
        print(name)
        delete_result = False
        if task_name == name:
            delete_result = True
        print(delete_result)
        return text_result, delete_result