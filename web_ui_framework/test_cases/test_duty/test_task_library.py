
import os
import pytest
import time
import yaml

from duty_pages.tasklibrary_page import TasklibraryPage

class TestLibraryPage:
    """履职管理-基础-任务库页面相关用例"""
    # datas_path = os.path.join(os.path.dirname(__file__),"content_datas.yaml")
    # content_datas = yaml.safe_load(open(datas_path,encoding='utf-8'))

    # @pytest.mark.zls
    def test_add_important_task(self,set_up_login):
        """验证添加重要任务成功"""
        driver = set_up_login
        task_page = TasklibraryPage(driver)
        task_page.open_tasklibrary()
        result_add = task_page.add_important_task()
        result_search = task_page.search_important_task()
        assert result_add[0] == result_search[0]

    # @pytest.mark.zls
    def test_add_other_task(self,set_up_login):
        """验证添加其他任务成功"""
        driver = set_up_login
        task_page = TasklibraryPage(driver)
        task_page.open_tasklibrary()
        result_add = task_page.add_other_task()
        result_search = task_page.search_other_task()
        assert result_add[0] == result_search[0]

    # @pytest.mark.zls
    def test_add_spot_task(self,set_up_login):
        """验证添加现场任务成功"""
        driver = set_up_login
        task_page = TasklibraryPage(driver)
        task_page.open_tasklibrary()
        result_add = task_page.add_spot_task()
        result_search = task_page.search_spot_task()
        assert result_add[0] == result_search[0]

    # @pytest.mark.zls
    def test_edit_important_task(self, set_up_login):
        """验证编辑重要任务成功"""
        driver = set_up_login
        task_page = TasklibraryPage(driver)
        task_page.open_tasklibrary()
        task_page.search_important_task()
        result = task_page.edit_important_task()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_edit_other_task(self, set_up_login):
        """验证编辑其他任务成功"""
        driver = set_up_login
        task_page = TasklibraryPage(driver)
        task_page.open_tasklibrary()
        task_page.search_other_task()
        result = task_page.edit_other_task()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_edit_spot_task(self, set_up_login):
        """验证编辑现场任务成功"""
        driver = set_up_login
        task_page = TasklibraryPage(driver)
        task_page.open_tasklibrary()
        task_page.search_spot_task()
        result = task_page.edit_spot_task()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_del_important_task(self, set_up_login):
        """验证删除重点任务成功"""
        driver = set_up_login
        task_page = TasklibraryPage(driver)
        task_page.open_tasklibrary()
        result = task_page.del_important_task()
        assert result == True

    # @pytest.mark.zls
    def test_del_other_task(self, set_up_login):
        """验证删除其他任务成功"""
        driver = set_up_login
        task_page = TasklibraryPage(driver)
        task_page.open_tasklibrary()
        result = task_page.del_other_task()
        assert result == True

    # @pytest.mark.zls
    def test_del_spot_task(self, set_up_login):
        """验证删除现场任务成功"""
        driver = set_up_login
        task_page = TasklibraryPage(driver)
        task_page.open_tasklibrary()
        result = task_page.del_spot_task()
        assert result == True