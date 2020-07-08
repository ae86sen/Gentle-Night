

import pytest
from basicdata_pages.employee_page import EmployeePage

class TestEmployee():
    """人员页面相关用例"""
    # @pytest.mark.zls
    def test_add_emp(self,set_up_login):
        """验证添加人员成功"""
        driver = set_up_login
        emp_page = EmployeePage(driver)
        emp_page.open_employee()
        result = emp_page.add_emp()
        assert result == 1

    # @pytest.mark.zls
    def test_edit_employee(self,set_up_login):
        """验证编辑人员信息成功"""
        driver = set_up_login
        emp_page = EmployeePage(driver)
        emp_page.open_employee()
        result = emp_page.edit_employee()
        assert result == True

    # @pytest.mark.zls
    def test_del_employee(self,set_up_login):
        """验证删除人员信息成功"""
        driver = set_up_login
        emp_page = EmployeePage(driver)
        emp_page.open_employee()
        result = emp_page.del_employee()
        assert result == False

    # @pytest.mark.zls
    def test_download_file(self,set_up_login):
        """验证导出人员信息成功"""
        driver = set_up_login
        emp_page = EmployeePage(driver)
        emp_page.open_employee()
        result = emp_page.download_file()
        assert result == True

    # @pytest.mark.zls
    def test_download_moudle(self,set_up_login):
        """验证下载导入模板成功"""
        driver = set_up_login
        emp_page = EmployeePage(driver)
        emp_page.open_employee()
        result = emp_page.download_moudle()
        assert result == True

    # @pytest.mark.zls
    def test_switch_org(self,set_up_login):
        """验证切换组织机构"""
        driver = set_up_login
        emp_page = EmployeePage(driver)
        emp_page.open_employee()
        result = emp_page.switch_org()
        assert result == True
