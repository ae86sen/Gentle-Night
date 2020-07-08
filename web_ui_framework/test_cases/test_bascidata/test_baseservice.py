
from basicdata_pages.baseservice_page import BaseServicePage


class TestBaseService():
    """基础服务页面相关用例"""
    def test_open(self,set_up_login):
        """验证基础页面能正常打开"""
        driver = set_up_login
        bs_page = BaseServicePage(driver)
        result = bs_page.open_baseservice()
        assert result=='基础服务'