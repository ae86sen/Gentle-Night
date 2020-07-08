
import os
import pytest
from basicdata_pages.organization_page import OrganizationPage
from common.constants import FILE_DIR
file_path = os.path.join(FILE_DIR,'org_upload.xls')
class TestOrganization():
    """基础服务页面相关用例"""

    # @pytest.mark.zls
    def test_add_org(self,set_up_login):
        """验证基础页面能正常打开"""
        driver = set_up_login
        org_page = OrganizationPage(driver)
        org_page.open_organization()
        result = org_page.add_org()
        assert result == 3

    # @pytest.mark.zls
    def test_upload_org(self,set_up_login):
        """验证导入组织机构成功"""
        driver = set_up_login
        org_page = OrganizationPage(driver)
        org_page.open_organization()
        result = org_page.upload_org(file_path)
        assert result == True

    # @pytest.mark.zls
    def test_export_org(self,set_up_login):
        """验证导出组织机构成功"""
        driver = set_up_login
        org_page = OrganizationPage(driver)
        org_page.open_organization()
        result = org_page.export_org()
        assert result == True

    # @pytest.mark.zls
    def test_download_moudle(self,set_up_login):
        """验证下载模板成功"""
        driver = set_up_login
        org_page = OrganizationPage(driver)
        org_page.open_organization()
        result = org_page.download_moudle()
        assert result == True