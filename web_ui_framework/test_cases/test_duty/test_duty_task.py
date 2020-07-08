
import time

import pytest

from duty_pages.dutytask_page import DutytaskPage

class TestDutyTaskPage:
    """履职管理-值班管理-值班任务页面相关用例"""

    # @pytest.mark.zls
    def test_add_duty_task(self,set_up_login):
        """验证批量添加值班任务成功"""
        driver = set_up_login
        duty_task_page = DutytaskPage(driver)
        duty_task_page.open_dutytask()
        results = duty_task_page.add_duty_task()
        assert results[0] +1 == results[1]

    # @pytest.mark.zls
    def test_check_result(self,set_up_login):
        """验证检查执行情况成功"""
        driver = set_up_login
        duty_task_page = DutytaskPage(driver)
        duty_task_page.open_dutytask()
        result = duty_task_page.check_result()
        assert result == True