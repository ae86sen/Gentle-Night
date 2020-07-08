
import pytest
import time

from map_pages.data_config_page import DataConfigPage

class TestDataConfig():
    """电子地图-数据配置页面相关用例"""

    @pytest.mark.skip
    def test_init_org(self, set_up_login):
        """验证初始化组织机构成功"""
        driver = set_up_login
        data_config_page = DataConfigPage(driver)
        data_config_page.open_data_config()
        result = data_config_page.init_org()

    @pytest.mark.skip
    def test_upload_gis(self, set_up_login):
        """验证上传GIS地图包成功"""
        driver = set_up_login
        data_config_page = DataConfigPage(driver)
        data_config_page.open_data_config()
        result = data_config_page.upload_gis()

    # @pytest.mark.zls
    def test_config_xm_service(self, set_up_login):
        """验证配置讯美地图服务成功"""
        driver = set_up_login
        data_config_page = DataConfigPage(driver)
        data_config_page.open_data_config()
        result = data_config_page.config_xm_service()
        return result == True