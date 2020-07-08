
import pytest
import time

from config_center_pages.vault_page import VaultPage
from datas.valut_equipment_datas import xpath_datas
class TestVault():
    """防范平台-远程值守页面相关用例"""

    # @pytest.mark.zls
    def test_edit_vault_name(self, set_up_login):
        """验证编辑金库名称成功"""
        driver = set_up_login
        vault_page = VaultPage(driver)
        vault_page.open_vault()
        edit_result = vault_page.edit_vault_name()
        assert edit_result == True

    # @pytest.mark.zls
    def test_edit_vault_param(self,set_up_login):
        """验证编辑金库默认参数成功"""
        driver = set_up_login
        vault_page = VaultPage(driver)
        vault_page.open_vault()
        result = vault_page.edit_vault_param()
        try:
            assert result == True
        except AssertionError as e:
            raise e
        else:
            vault_page.edit_vault_param_clear()

    # @pytest.mark.zls
    @pytest.mark.parametrize("data",xpath_datas)
    def test_add_equipment(self,data,set_up_login):
        tab_xpath = data["tab"]
        add_xpath = data["add"]
        form_xpath = data["form"]
        driver = set_up_login
        vault_page = VaultPage(driver)
        vault_page.open_vault()
        result = vault_page.add_equipment(tab_xpath,add_xpath,form_xpath)
        assert result == True

    # @pytest.mark.zls
    @pytest.mark.parametrize("data", xpath_datas)
    def test_del_equipment(self,data,set_up_login):
        tab_xpath = data["tab"]
        del_xpath = data["add"]
        form_xpath = data["form"]
        driver = set_up_login
        vault_page = VaultPage(driver)
        vault_page.open_vault()
        result = vault_page.del_equipment(tab_xpath, del_xpath, form_xpath)
        assert result == True

    # @pytest.mark.zls
    def test_config_output(self,set_up_login):
        driver = set_up_login
        vault_page = VaultPage(driver)
        vault_page.open_vault()
        result = vault_page.config_output()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_add_view(self,set_up_login):
        driver = set_up_login
        vault_page = VaultPage(driver)
        vault_page.open_vault()
        result = vault_page.add_view()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_del_view(self,set_up_login):
        driver = set_up_login
        vault_page = VaultPage(driver)
        vault_page.open_vault()
        result = vault_page.del_view()
        assert result[0] == result[1] + 1

    # @pytest.mark.zls
    def test_add_golden(self,set_up_login):
        driver = set_up_login
        vault_page = VaultPage(driver)
        vault_page.open_vault()
        result = vault_page.add_golden()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_del_golden(self, set_up_login):
        driver = set_up_login
        vault_page = VaultPage(driver)
        vault_page.open_vault()
        result = vault_page.del_golden()
        assert result[0] == result[1] + 1