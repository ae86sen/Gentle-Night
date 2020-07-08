

from urllib import parse

import pytest
import time

from equipment_pages.alarmhost_page import AlarmHostPage

class TestAlarmHost():
    """报警主机页面相关用例"""

    # @pytest.mark.zls
    def test_switch_tab(self, set_up_login):
        """验证切换tab标签页成功"""
        driver = set_up_login
        alarm_page = AlarmHostPage(driver)
        alarm_page.open_alarm()
        host_url = alarm_page.switch_to_alarm_host()
        assert "tab=alarmHost" in host_url
        system_url = alarm_page.switch_to_alarm_system()
        assert "tab=alarmsubsystem" in system_url
        zone_url = alarm_page.switch_to_alarm_zone()
        assert "tab=alarmzone" in zone_url
        alarm_output_url = alarm_page.switch_to_alarm_output()
        assert "tab=alarmOutput" in alarm_output_url

    # @pytest.mark.zls
    def test_switch_org(self, set_up_login):
        """验证切换组织机构成功"""
        driver = set_up_login
        alarm_page = AlarmHostPage(driver)
        alarm_page.open_alarm()
        result = alarm_page.switch_org()
        url = driver.current_url
        text = (url.split('='))[-1]
        # url中含有中文，进行解码
        expected = parse.unquote(text)
        assert result == expected

    # @pytest.mark.zls
    def test_add_alarm(self,set_up_login):
        """验证添加2个报警服务->同步->编辑->删除任意报警服务成功"""
        driver = set_up_login
        alarm_page = AlarmHostPage(driver)
        alarm_page.open_alarm()
        # 添加2个报警服务
        for i in range(2):
            assert alarm_page.add_alarm_service() == True
        driver.refresh()
        # 同步第一个报警服务
        assert alarm_page.sync_alarm_service() == True
        driver.refresh()
        # 编辑第一个报警服务
        assert alarm_page.edit_alarm_service() == True
        driver.refresh()
        # 删除第一个报警服务
        assert alarm_page.del_alarm_service() == True

