

import pytest
import time

from map_pages.plane_map_page import PlaneMapPage

class TestPlaneMap():
    """电子地图-平面地图页面相关用例"""

    # @pytest.mark.zls
    def test_switch_org(self, set_up_login):
        """验证切换组织机构成功"""
        driver = set_up_login
        plane_map_page = PlaneMapPage(driver)
        plane_map_page.open_plane_map()
        result = plane_map_page.switch_org()
        assert result == True

    # @pytest.mark.zls
    def test_switch_device(self,set_up_login):
        """验证切换设备"""
        driver = set_up_login
        plane_map_page = PlaneMapPage(driver)
        plane_map_page.open_plane_map()
        results = plane_map_page.switch_device()
        for i in results:
            assert i == 'true'

