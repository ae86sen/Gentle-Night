

import pytest
import time

from alarm_manage_pages.alarmlink_page import AlarmLinkPage

class TestAlarmLink():
    """联动规则页面相关用例"""

    # @pytest.mark.zls
    def test_add_alarm_link(self, set_up_login):
        """验证添加联动规则成功"""
        driver = set_up_login
        alarm_link_page = AlarmLinkPage(driver)
        alarm_link_page.open_alarmlink()
        add_result_logo,add_result_data = alarm_link_page.add_alarm_link()
        assert add_result_logo == True
        assert add_result_data == True

    # @pytest.mark.zls
    def test_edit_alarm_link(self, set_up_login):
        """验证编辑联动规则成功"""
        driver = set_up_login
        alarm_link_page = AlarmLinkPage(driver)
        alarm_link_page.open_alarmlink()
        edit_result_logo,edit_result_data = alarm_link_page.edit_alarm_link()
        assert edit_result_logo == True
        assert edit_result_data == True

    # @pytest.mark.zls
    def test_del_alarm_link(self, set_up_login):
        """验证删除联动规则成功"""
        driver = set_up_login
        alarm_link_page = AlarmLinkPage(driver)
        alarm_link_page.open_alarmlink()
        del_result_data = alarm_link_page.del_alarm_link()
        assert del_result_data == False
