
import pytest
import yaml

from config_center_pages.client_manage_page import ClientManagePage
import os
datas_path = os.path.join(os.path.dirname(__file__),"client_manage_datas.yaml")

class TestClientManage():
    """防范平台-客户端管理页面相关用例"""
    client_manage_datas = yaml.safe_load(open(datas_path,encoding='utf-8'))

    # @pytest.mark.zls
    @pytest.mark.parametrize("time",client_manage_datas)
    def test_set_normal_time(self, time, set_up_login):
        """验证设置时间成功"""
        driver = set_up_login
        client_manage_page = ClientManagePage(driver)
        client_manage_page.open_client_manage()
        result = client_manage_page.set_normal_time(time)
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_set_less_boundary(self,set_up_login):
        """验证设置时间为0显示不关闭"""
        driver = set_up_login
        client_manage_page = ClientManagePage(driver)
        client_manage_page.open_client_manage()
        result = client_manage_page.set_less_boundary_time()
        assert result[0] == "不关闭"

    # @pytest.mark.zls
    def test_set_greater_boundary(self, set_up_login):
        """验证设置时间为91弹出错误提示"""
        driver = set_up_login
        client_manage_page = ClientManagePage(driver)
        client_manage_page.open_client_manage()
        result = client_manage_page.set_greater_boundary_time()
        assert result[0] == "关闭时间必须在1-90之间!"