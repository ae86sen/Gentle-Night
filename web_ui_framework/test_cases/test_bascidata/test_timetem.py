import pytest
from basicdata_pages.timetemplate_page import TimetempPage

class TestTimetem():
    """时间模板页面相关用例"""

    # @pytest.mark.zls
    def test_add_time(self,set_up_login):
        """验证添加时间模板成功"""
        driver = set_up_login
        time_page = TimetempPage(driver)
        time_page.open_timetemp()
        result = time_page.add_time_temp()
        assert result == 1