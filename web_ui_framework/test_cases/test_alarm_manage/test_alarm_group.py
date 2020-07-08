

import pytest
import time

from alarm_manage_pages.alarmgroup_page import AlarmGroupPage

class TestAlarmGroup():
    """报警源分组页面相关用例"""

    # @pytest.mark.zls
    def test_add_alarm_group(self, set_up_login):
        """验证添加报警源分组成功"""
        driver = set_up_login
        alarm_group_page = AlarmGroupPage(driver)
        alarm_group_page.open_alarmgroup()
        add_result_logo= alarm_group_page.add_as_group()
        assert add_result_logo == True

    # @pytest.mark.zls
    def test_edit_alarm_group(self,set_up_login):
        """验证编辑报警源分组成功"""
        driver = set_up_login
        alarm_group_page = AlarmGroupPage(driver)
        alarm_group_page.open_alarmgroup()
        edit_result_logo, edit_result_data = alarm_group_page.edit_as_group()
        assert edit_result_logo == True
        assert edit_result_data == True

    # @pytest.mark.zls
    def test_del_alarm_group(self, set_up_login):
        """验证删除报警源分组成功"""
        driver = set_up_login
        alarm_group_page = AlarmGroupPage(driver)
        alarm_group_page.open_alarmgroup()
        del_result_logo,del_result_data = alarm_group_page.del_as_group()
        assert del_result_logo == True
        assert del_result_data == False
