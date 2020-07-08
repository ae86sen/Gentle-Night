
import pytest
from basicdata_pages.role_page import RolePage

class TestRole():
    """角色页面相关用例"""

    def test_add_role(self,set_up_login):
        """验证添加角色成功"""
        driver = set_up_login
        role_page = RolePage(driver)
        role_page.open_role()
        result = role_page.add_role()
        assert result == "auto_test"

    # @pytest.mark.zls
    def test_edit_role(self,set_up_login):
        """验证编辑角色成功"""
        driver = set_up_login
        role_page = RolePage(driver)
        role_page.open_role()
        result = role_page.edit_role()
        assert result == True

    # @pytest.mark.zls
    def test_del_role(self, set_up_login):
        """验证删除角色成功"""
        driver = set_up_login
        role_page = RolePage(driver)
        role_page.open_role()
        result = role_page.del_role()
        assert result == False


    # @pytest.mark.zls
    def test_download_file(self,set_up_login):
        """验证导出角色信息成功"""
        driver = set_up_login
        role_page = RolePage(driver)
        role_page.open_role()
        result = role_page.download_file()
        assert result == True

    # @pytest.mark.zls
    def test_download_moudle(self,set_up_login):
        """验证下载导入模板成功"""
        driver = set_up_login
        role_page = RolePage(driver)
        role_page.open_role()
        result = role_page.download_moudle()
        assert result == True