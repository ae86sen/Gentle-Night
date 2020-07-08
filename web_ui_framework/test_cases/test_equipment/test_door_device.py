
from urllib import parse

import pytest
from equipment_pages.door_page import DoorPage

class TestDoor():
    """门禁页面相关用例"""

    # @pytest.mark.zls
    def test_switch_tab(self, set_up_login):
        """验证切换tab标签页成功"""
        driver = set_up_login
        door_page = DoorPage(driver)
        door_page.open_door()
        control_url = door_page.switch_to_control()
        assert "tab=control" in control_url
        doors_url = door_page.switch_to_doors()
        assert "tab=doors" in doors_url
        card_reading_url = door_page.switch_to_card_reading()
        assert "tab=cardReading" in card_reading_url
        card_holder_url = door_page.switch_to_card_holder()
        assert "tab=cardHolder" in card_holder_url
        control_alarm_url = door_page.switch_to_alarm_control()
        assert "tab=controlAlarm" in control_alarm_url

    # @pytest.mark.zls
    def test_add_door(self, set_up_login):
        """验证添加2个门禁服务->同步->编辑->删除任意门禁服务成功"""
        driver = set_up_login
        door_page = DoorPage(driver)
        door_page.open_door()
        # 添加2个门禁服务
        for i in range(2):
            assert door_page.add_door_service() == True
        driver.refresh()
        # 同步第一个门禁服务
        assert door_page.sync_door_service() == True
        driver.refresh()
        # 编辑第一个门禁服务
        assert door_page.edit_door_service() == True
        driver.refresh()
        # 删除第一个门禁服务
        assert door_page.del_door_service() == True


    # @pytest.mark.zls
    def test_switch_org(self, set_up_login):
        """验证切换组织机构成功"""
        driver = set_up_login
        door_page = DoorPage(driver)
        door_page.open_door()
        result = door_page.switch_org()
        url = driver.current_url
        text = (url.split('='))[-1]
        # url中含有中文，进行解码
        expected = parse.unquote(text)
        assert result == expected