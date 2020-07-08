
import pytest
from equipment_pages.tvwall_page import TvWallPage

class TestTvWall():
    """电视墙页面相关用例"""

    # @pytest.mark.zls
    def test_edit_conf(self,set_up_login):
        """验证电视墙配置视图->配置走马灯->保存配置成功"""
        driver = set_up_login
        tvwall_page = TvWallPage(driver)
        tvwall_page.open_tvwall()
        result = tvwall_page.edit_view()
        assert result == True
        result2 = tvwall_page.save_conf()
        assert result2 == True