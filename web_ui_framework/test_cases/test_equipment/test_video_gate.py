

import pytest
import time

from equipment_pages.videogate_page import VideoGatePage

@pytest.mark.skip
class TestVideoGatePage:
    """视频网关页面相关用例"""

    # @pytest.mark.zls
    def test_edit_gate(self, set_up_login):
        """验证编辑网关信息成功"""
        driver = set_up_login
        gate_page = VideoGatePage(driver)
        gate_page.open_videogate()
        result = gate_page.edit_gate()
        assert result == True

    # @pytest.mark.zls
    def test_authorize_gate(self,set_up_login):
        """授权网关"""
        driver = set_up_login
        gate_page = VideoGatePage(driver)
        gate_page.open_videogate()
        result = gate_page.authorize_gate()
        assert result == True


    def test_rest_gate(self,set_up_login):
        """重置网关"""
        """注：该用例执行时间需要30分钟"""
        driver = set_up_login
        gate_page = VideoGatePage(driver)
        gate_page.open_videogate()
        result = gate_page.reset_gate()
        assert result == 6