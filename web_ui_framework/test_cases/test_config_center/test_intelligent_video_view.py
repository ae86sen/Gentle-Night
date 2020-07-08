

import pytest
import time

from config_center_pages.intelligent_video_view_page import IVVPage

class TestIVV():
    """防范平台-智能视图轮巡页面相关用例"""

    # @pytest.mark.zls
    def test_add_ivv(self, set_up_login):
        """验证添加智能视图成功"""
        driver = set_up_login
        ivv_page = IVVPage(driver)
        ivv_page.open_ivv()
        add_result_logo,add_result_data = ivv_page.add_ivv()
        assert add_result_logo == True
        assert add_result_data == True

    def test_edit_ivv(self, set_up_login):
        """验证编辑智能视图成功"""
        driver = set_up_login
        ivv_page = IVVPage(driver)
        ivv_page.open_ivv()
        edit_result_logo,edit_result_data = ivv_page.edit_ivv()
        assert edit_result_logo == True
        assert edit_result_data == True

    def test_del_ivv(self,set_up_login):
        """验证删除能视图成功"""
        driver = set_up_login
        ivv_page = IVVPage(driver)
        ivv_page.open_ivv()
        del_result_logo,del_result_data = ivv_page.del_ivv()
        assert del_result_logo == True
        assert del_result_data == False