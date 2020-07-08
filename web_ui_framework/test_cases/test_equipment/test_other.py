

import pytest
import time

from equipment_pages.other_page import OtherPage

class TestOther():
    """其它设备页面相关用例"""

    # @pytest.mark.zls
    def test_led(self, set_up_login):
        """验证添加led->编辑->删除成功"""
        driver = set_up_login
        other_page = OtherPage(driver)
        other_page.open_other()
        # 添加
        add_result_data,name = other_page.add_led()
        assert add_result_data == True
        driver.refresh()
        time.sleep(0.5)
        # 编辑
        edit_result_logo,edit_result_data,new_name = other_page.edit_led(name)
        assert edit_result_logo == True
        assert edit_result_data == True
        driver.refresh()
        time.sleep(0.5)
        # 删除
        del_result_logo,del_result_data = other_page.del_led(new_name)
        assert del_result_logo == True
        assert del_result_data == False

    # @pytest.mark.zls
    def test_meter(self,set_up_login):
        """验证添加温湿度探头->编辑->删除成功"""
        driver = set_up_login
        other_page = OtherPage(driver)
        other_page.open_other()
        # 添加
        result1 = other_page.add_meter()
        assert result1 == True
        driver.refresh()
        # 编辑
        result2 = other_page.edit_meter()
        assert result2 == True
        driver.refresh()
        # 删除
        result3 = other_page.del_meter()
        assert result3 == True

    # @pytest.mark.zls
    def test_sms(self,set_up_login):
        """验证添加SMS短信设备->编辑->删除成功"""
        driver = set_up_login
        other_page = OtherPage(driver)
        other_page.open_other()
        result1 = other_page.add_sms()
        assert result1 == True
        result2 = other_page.edit_sms()
        assert result2 == True
        result3 = other_page.del_sms()
        assert result3 == True
