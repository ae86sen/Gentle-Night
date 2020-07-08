
import os
import pytest
import yaml

from duty_pages.spotins_page import SpotinsPage

class TestSpotinsPage():
    '''履职管理-现场检查相关用例'''
    data_path = os.path.join(os.path.dirname(__file__), "spotins_datas.yaml")
    spotins_data = yaml.safe_load(open(data_path, encoding='utf-8'))

    #@pytest.mark.yd
    def test_check_state_contents(self,set_up_login):
        '''检查状态下拉框元素'''
        driver = set_up_login
        spo_page = SpotinsPage(driver)
        spo_page.open_spotinspection()

        result = spo_page.check_state_contents()
        for i in result:
            print(i,end=",")
        assert result[0] == '全部'
        assert result[1] == '未到执行时间'
        assert result[2] == '待执行'
        assert result[3] == '执行中'
        assert result[4] == '完成待提交'
        assert result[5] == '完成'
        assert result[6] == '超时完成'
        assert result[7] == '超时未完成'

    #@pytest.mark.yd
    def test_add_task(self,set_up_login):
        '''添加现场任务 '''
        driver = set_up_login
        spo_page = SpotinsPage(driver)
        spo_page.open_spotinspection()

        name_task = spo_page.check_add_task("autoTest")
       # print(name_task)
        assert name_task[0] == "autoTest"

    # @pytest.mark.zls
    @pytest.mark.parametrize("data",spotins_data)
    def test_selct_by_name(self,data,set_up_login):
        '''通过名字搜索 '''
        driver = set_up_login
        spo_page = SpotinsPage(driver)
        spo_page.open_spotinspection()

        name = spo_page.selct_by_name(data)
        assert name[0] == "autoTest"

    # @pytest.mark.zls
    # def test_selct_by_person(self, set_up_login):
    #     '''通过执行人搜索 '''
    #     driver = set_up_login
    #     spo_page = SpotinsPage(driver)
    #     spo_page.open_spotinspection()
    #
    #     person = spo_page.selct_by_person("t181027")
    #     person_s = ' '.join(person)
    #     print(type(person_s),person_s)
    #     assert "t181027" in person_s
    #
    # @pytest.mark.zls
    # def test_selct_by_content(self, set_up_login):
    #     '''通过内容搜索 '''
    #     driver = set_up_login
    #     spo_page = SpotinsPage(driver)
    #     spo_page.open_spotinspection()
    #
    #     content = spo_page.selct_by_content("金库大门")
    #     content_s = ' '.join(content)
    #     assert "金库大门" in content_s


    #@pytest.mark.yd
    def test_check_delete_unexecuted(self, set_up_login):
        '''删除未到执行时间的任务 '''
        driver = set_up_login
        spo_page = SpotinsPage(driver)
        spo_page.open_spotinspection()

        result1,result2 = spo_page.check_delete_unexecuted()

        assert result1 == True
        assert result2 == False

    #@pytest.mark.yd
    def test_check_details_button(self, set_up_login):
        '''查看执行情况详情 '''
        driver = set_up_login
        spo_page = SpotinsPage(driver)
        spo_page.open_spotinspection()
        title = spo_page.check_details_button()
        assert "现场检查执行情况" in title
