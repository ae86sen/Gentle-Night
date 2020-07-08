
from urllib import parse

import pytest
import time

from equipment_pages.sdaalarm_page import SdaAlarmPage
from equipment_pages.videogate_page import VideoGatePage

class TestSdaAlarm():
    """虚拟事件设备页面相关用例"""

    # @pytest.mark.zls
    def test_switch_org(self,set_up_login):
        """验证切换组织机构成功"""
        driver = set_up_login
        sda_alarm_page = SdaAlarmPage(driver)
        sda_alarm_page.open_sdalarm()
        result = sda_alarm_page.switch_org()
        url = driver.current_url
        text = (url.split('='))[-1]
        # url中含有中文，进行解码
        expected = parse.unquote(text)
        assert result == expected

    # @pytest.mark.zls
    def test_add_device(self,set_up_login):
        """验证添加虚拟事件设备->编辑->复制主机->移动组织机构成功"""
        driver = set_up_login
        sda_alarm_page = SdaAlarmPage(driver)
        sda_alarm_page.open_sdalarm()
        # 添加设备
        add_result_logo,add_result_data = sda_alarm_page.add_host()
        assert add_result_logo == True,"添加成功图标未找到"
        assert add_result_data == True,"新增数据未在页面中找到"

    # @pytest.mark.zls
    def test_edit_device(self,set_up_login):
        driver = set_up_login
        sda_alarm_page = SdaAlarmPage(driver)
        sda_alarm_page.open_sdalarm()
        # 编辑设备
        edit_result_logo,edit_result_data = sda_alarm_page.edit_host()
        assert edit_result_logo == True,"编辑成功图标未找到"
        assert edit_result_data == True,"修改后的数据未在页面中找到"

    # @pytest.mark.zls
    def test_copy_device(self, set_up_login):
        driver = set_up_login
        sda_alarm_page = SdaAlarmPage(driver)
        sda_alarm_page.open_sdalarm()
        # 复制设备
        copy_result_logo,copy_result_data = sda_alarm_page.copy_host()
        assert copy_result_logo == True,"复制成功图标未找到"
        assert copy_result_data == True,"在下级机构中未找到复制主机"

    # @pytest.mark.zls
    def test_search_device(self,set_up_login):
        driver = set_up_login
        sda_alarm_page = SdaAlarmPage(driver)
        sda_alarm_page.open_sdalarm()
        result = sda_alarm_page.search_host()
        assert result == True

    def test_move_org(self, set_up_login):
        driver = set_up_login
        sda_alarm_page = SdaAlarmPage(driver)
        sda_alarm_page.open_sdalarm()
        # 移动组织机构
        # result = sda_alarm_page.move_org()
        # assert result == True

    # @pytest.mark.zls
    def test_del_host(self, set_up_login):
        """验证删除虚拟设备主机成功"""
        driver = set_up_login
        sda_alarm_page = SdaAlarmPage(driver)
        sda_alarm_page.open_sdalarm()
        del_result_logo,del_result_data = sda_alarm_page.del_host()
        assert del_result_logo == True,"删除成功图标未找到"
        assert del_result_data == False,"页面中还存在已删除设备信息"
