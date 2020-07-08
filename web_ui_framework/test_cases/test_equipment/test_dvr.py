
import os
import pytest
from equipment_pages.dvr_page import DvrPage
from urllib import parse
from common.constants import FILE_DIR
file_path = os.path.join(FILE_DIR,'dvr_import.xls')
class TestDvr():
    """视频设备页面相关用例"""

    def test_switch_tab(self,set_up_login):
        """验证切换tab标签页成功"""
        driver = set_up_login
        dvr_page = DvrPage(driver)
        dvr_page.open_dvr()
        dvs_url = dvr_page.switch_to_dvs()
        assert "tab=dvs" in dvs_url
        camera_url = dvr_page.switch_to_camera()
        assert  "tab=camera" in camera_url
        alarm_input_url = dvr_page.switch_to_alarm_input()
        assert "tab=alarmInput" in alarm_input_url
        alarm_output_url = dvr_page.switch_to_alarm_output()
        assert "tab=alarmOutput" in alarm_output_url
        ip_talk_url = dvr_page.switch_to_ip_talk()
        assert "tab=ipTalk" in ip_talk_url

    # @pytest.mark.zls
    def test_download_template(self,set_up_login):
        """验证导出模板成功"""
        driver = set_up_login
        dvr_page = DvrPage(driver)
        dvr_page.open_dvr()
        result = dvr_page.download_dvr_template()
        assert result == True

    # @pytest.mark.zls
    def test_download_imp_tem(self,set_up_login):
        """验证导入模板下载成功"""
        driver = set_up_login
        dvr_page = DvrPage(driver)
        dvr_page.open_dvr()
        result = dvr_page.download_imp_tem()
        assert result == True

    # @pytest.mark.zls
    def test_import_file(self,set_up_login):
        """验证导入视频设备成功"""
        driver = set_up_login
        dvr_page = DvrPage(driver)
        dvr_page.open_dvr()
        result = dvr_page.import_file(file_path)
        return result == True

    # @pytest.mark.zls
    def test_batch_add_dvs(self,set_up_login):
        """验证批量添加设备成功"""
        driver = set_up_login
        dvr_page = DvrPage(driver)
        dvr_page.open_dvr()
        result = dvr_page.batch_add_dvs()
        return result == True

    # @pytest.mark.zls
    def test_search_device(self, set_up_login):
        """验证搜索设备成功"""
        driver = set_up_login
        dvr_page = DvrPage(driver)
        dvr_page.open_dvr()
        result = dvr_page.search_device()
        assert result == True

    # @pytest.mark.zls
    def test_del_device(self, set_up_login):
        """验证删除设备成功"""
        driver = set_up_login
        dvr_page = DvrPage(driver)
        dvr_page.open_dvr()
        result = dvr_page.del_device()
        assert result == False

    # @pytest.mark.zls
    def test_switch_org(self, set_up_login):
        """验证切换组织机构成功"""
        driver = set_up_login
        dvr_page = DvrPage(driver)
        dvr_page.open_dvr()
        result = dvr_page.switch_org()
        url = driver.current_url
        text = (url.split('='))[-1]
        # url中含有中文，进行解码
        expected = parse.unquote(text)
        assert result == expected

