

import pytest
import time

from system_manage_pages.service_page import ServicePage

class TestService():
    """安装服务页面相关用例"""

    # @pytest.mark.zls
    def test_download_agent(self, set_up_login):
        """验证下载代理成功"""
        driver = set_up_login
        service_page = ServicePage(driver)
        service_page.open_service()
        result = service_page.download_agent()
        assert result == True