

import pytest
import time

from config_center_pages.manual_rotation_page import ManualRotationPage

class TestManualRotation():
    """防范平台-风险时段手动轮巡页面相关用例"""

    # @pytest.mark.zls
    def test_add_rule(self, set_up_login):
        """验证添加风险时段手动轮巡规则成功"""
        driver = set_up_login
        mr_page = ManualRotationPage(driver)
        mr_page.open_mr()
        add_result_logo,add_result_data = mr_page.add_rule()
        assert add_result_data == True

    # @pytest.mark.zls
    def test_edit_rule(self,set_up_login):
        """验证编辑风险时段手动轮巡规则成功"""
        driver = set_up_login
        mr_page = ManualRotationPage(driver)
        mr_page.open_mr()
        edit_result_logo, edit_result_data = mr_page.edit_rule()
        assert edit_result_logo == True
        assert edit_result_data == True

    # @pytest.mark.zls
    def test_del_rule(self,set_up_login):
        """验证删除风险时段手动轮巡规则成功"""
        driver = set_up_login
        mr_page = ManualRotationPage(driver)
        mr_page.open_mr()
        del_result_logo,del_result_data = mr_page.del_rule()
        assert del_result_logo == True
        assert del_result_data == False
