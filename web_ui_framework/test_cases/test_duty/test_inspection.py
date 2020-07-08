

import time

import os
import pytest
import yaml

from duty_pages.inspection_page import InspectionPage


class TestInspectionPage:
    """履职管理-非现场检查页面相关用例"""
    data_path = os.path.join(os.path.dirname(__file__), "inspection_datas.yaml")
    inspection_data = yaml.safe_load(open(data_path, encoding='utf-8'))

    # @pytest.mark.zls
    def test_check_type(self, set_up_login):
        """验证类型下拉框"""
        driver = set_up_login
        ins_page = InspectionPage(driver)
        ins_page.open_inspection()
        results = ins_page.check_type()
        assert results[0] == '全部'
        assert results[1] == '重点任务'
        assert results[2] == '其他任务'

    # @pytest.mark.zls
    def test_check_status(self, set_up_login):
        """验证状态下拉框"""
        driver = set_up_login
        ins_page = InspectionPage(driver)
        ins_page.open_inspection()
        results = ins_page.check_status()
        assert results[0] == '全部'
        assert results[1] == '未到执行时间'
        assert results[2] == '待执行'
        assert results[3] == '执行中'
        assert results[4] == '完成待提交'
        assert results[5] == '完成'
        assert results[6] == '超时完成'
        assert results[7] == '超时未完成'

    # @pytest.mark.zls
    def test_add_important_task(self, set_up_login):
        """验证添加重要任务成功"""
        driver = set_up_login
        ins_page = InspectionPage(driver)
        ins_page.open_inspection()
        result = ins_page.add_important_task()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_add_other_task(self, set_up_login):
        """验证添加其它任务成功"""
        driver = set_up_login
        ins_page = InspectionPage(driver)
        ins_page.open_inspection()
        result = ins_page.add_other_task()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_search_by_name(self, set_up_login):
        """验证通过任务名称搜索成功"""
        driver = set_up_login
        ins_page = InspectionPage(driver)
        ins_page.open_inspection()
        result = ins_page.search_by_name()
        assert result[0] == result[1]

    # @pytest.mark.zls
    def test_search_by_worker(self, set_up_login):
        """验证通过任务执行人搜索成功"""
        driver = set_up_login
        ins_page = InspectionPage(driver)
        ins_page.open_inspection()
        result = ins_page.search_by_worker()
        assert result == True

    # @pytest.mark.zls
    def test_search_by_content(self, set_up_login):
        """验证通过任务内容搜索成功"""
        driver = set_up_login
        ins_page = InspectionPage(driver)
        ins_page.open_inspection()
        result = ins_page.search_by_content()
        assert result == True

    # @pytest.mark.zls
    @pytest.mark.parametrize("loc", inspection_data)
    def test_batch_add_important_task(self, loc,set_up_login):
        """验证批量添加重点任务成功"""
        driver = set_up_login
        ins_page = InspectionPage(driver)
        ins_page.open_inspection()
        result = ins_page.batch_add_important_task(loc)
        assert result == True

    # @pytest.mark.zls
    @pytest.mark.parametrize("loc", inspection_data)
    def test_batch_add_other_task(self, loc,set_up_login):
        """验证批量添加其他任务成功"""
        driver = set_up_login
        ins_page = InspectionPage(driver)
        ins_page.open_inspection()
        result = ins_page.batch_add_other_task(loc)
        assert result == True
