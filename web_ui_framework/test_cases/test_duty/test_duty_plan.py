
import time

import pytest

from duty_pages.dutyplan_page import DutyPlanPage

class TestDutyPlanPage:
    """履职管理-值班管理-值班计划页面相关用例"""

    # @pytest.mark.zls
    def test_batch_add_plan(self,set_up_login):
        """验证批量添加值班计划成功"""
        driver = set_up_login
        duty_plan_page = DutyPlanPage(driver)
        duty_plan_page.open_dutyplan()
        result = duty_plan_page.batch_add_plan()
        assert result == True

    # @pytest.mark.zls
    def test_setting(self,set_up_login):
        """验证设置偏差成功"""
        driver = set_up_login
        duty_plan_page = DutyPlanPage(driver)
        duty_plan_page.open_dutyplan()
        result = duty_plan_page.setting()
        assert result == True

    # @pytest.mark.zls
    def test_prevent_sleep(self,set_up_login):
        """验证防瞌睡成功"""
        driver = set_up_login
        duty_plan_page = DutyPlanPage(driver)
        duty_plan_page.open_dutyplan()
        try:
            result = duty_plan_page.prevent_sleep()
            assert result == True
        except Exception as e:
            raise e
        else:
            duty_plan_page.prevent_sleep_clear()
