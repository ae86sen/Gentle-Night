

import pytest
import time

from equipment_pages.res_group_page import ResGroupPage
from datas.res_group_datas import xpath_datas


class TestResGroup():
    """资源分组页面相关用例"""

    @pytest.mark.parametrize("data",xpath_datas)
    # @pytest.mark.zls
    def test_add_dynamic_cg(self,data,set_up_login):
        """验证添加动态分组成功"""
        tab_xpath = data["tab"]
        add_xpath = data["add"]
        driver = set_up_login
        res_group_page = ResGroupPage(driver)
        res_group_page.open_resgroup()
        # 添加动态分组
        add_result_logo,add_result_data = res_group_page.add_dynamic_group(tab_xpath,add_xpath)
        assert add_result_logo == True
        assert add_result_data == True

    @pytest.mark.parametrize("data", xpath_datas)
    # @pytest.mark.zls
    def test_add_to_del_static_cg(self,data,set_up_login):
        """验证添加-编辑-删除静态分组成功"""
        tab_xpath = data["tab"]
        add_xpath = data["add"]
        driver = set_up_login
        res_group_page = ResGroupPage(driver)
        res_group_page.open_resgroup()
        # 添加静态分组
        add_result_logo,add_result_data,name = res_group_page.add_static_group(tab_xpath,add_xpath)
        assert add_result_logo == True
        assert add_result_data == True
        time.sleep(1.5)
        # 编辑静态分组
        edit_result_logo, edit_result_data, new_name = res_group_page.edit_static_group(tab_xpath,name)
        assert edit_result_logo == True
        assert edit_result_data == True
        time.sleep(1.5)
        # 删除静态分组
        del_result_logo, del_result_data = res_group_page.del_static_group(tab_xpath,new_name)
        assert del_result_logo == True
        assert del_result_data == False

