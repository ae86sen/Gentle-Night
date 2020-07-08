

import pytest
from basicdata_pages.tag_page import TagPage

class TestTag():
    """标签管理页面相关用例"""

    # @pytest.mark.zls
    def test_add_tag(self,set_up_login):
        """验证添加标签成功"""
        driver = set_up_login
        tag_page = TagPage(driver)
        tag_page.open_tag()
        result = tag_page.add_tag()
        assert result == True

    # @pytest.mark.zls
    def test_del_tag(self,set_up_login):
        """验证删除标签成功"""
        driver = set_up_login
        tag_page = TagPage(driver)
        tag_page.open_tag()
        result = tag_page.del_tag()
        assert result == False