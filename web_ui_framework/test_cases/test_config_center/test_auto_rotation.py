
import pytest
import time

from config_center_pages.auto_rotation_page import AutoRotationPage

class TestAutoRotation():
    """防范平台-定时轮巡页面相关用例"""

    # @pytest.mark.zls
    def test_add_rule(self, set_up_login):
        """验证添加定时轮巡规则成功"""
        driver = set_up_login
        ar_page = AutoRotationPage(driver)
        ar_page.open_ar()
        add_result_logo,add_result_data = ar_page.add_rule()
        assert add_result_logo == True
        assert add_result_data == True

    # @pytest.mark.zls
    def test_edit_rule(self, set_up_login):
        """验证编辑定时轮巡规则成功"""
        driver = set_up_login
        ar_page = AutoRotationPage(driver)
        ar_page.open_ar()
        edit_result_logo,edit_result_data = ar_page.edit_rule()
        assert edit_result_logo == True
        assert edit_result_data == True

    # @pytest.mark.zls
    def test_del_rule(self, set_up_login):
        """验证删除定时轮巡规则成功"""
        driver = set_up_login
        ar_page = AutoRotationPage(driver)
        ar_page.open_ar()
        del_result_logo, del_result_data = ar_page.del_rule()
        assert del_result_logo == True
        assert del_result_data == False