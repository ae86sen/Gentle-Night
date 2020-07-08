
import os
import pytest
import yaml

from duty_pages.content_page import ContentPage

class TestContent:
    """履职管理-基础-检查内容页面相关用例"""
    datas_path = os.path.join(os.path.dirname(__file__),"content_datas.yaml")
    content_datas = yaml.safe_load(open(datas_path,encoding='utf-8'))

    @pytest.mark.zls
    @pytest.mark.parametrize("data",content_datas)
    def test_add_content(self,data,set_up_login):
        """验证添加内容成功"""
        driver = set_up_login
        content_page = ContentPage(driver)
        content_page.open_content()
        result = content_page.add_content(data)
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_add_content_none(self, set_up_login):
        """验证添加内容为空"""
        driver = set_up_login
        content_page = ContentPage(driver)
        content_page.open_content()
        result = content_page.add_content_none()
        assert result[0] == "内容必填"

    # @pytest.mark.zls
    def test_copy_content(self, set_up_login):
        """验证复制内容成功"""
        driver = set_up_login
        content_page = ContentPage(driver)
        content_page.open_content()
        result = content_page.copy_content()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_del_content(self, set_up_login):
        """验证删除内容成功"""
        driver = set_up_login
        content_page = ContentPage(driver)
        content_page.open_content()
        result = content_page.del_content()
        assert result[0] == result[1] + 1

