
from urllib import parse

import os
import pytest

from common.constants import FILE_DIR
from equipment_pages.ipvoice_page import IPVoicePage

class TestIPVoice():
    """语音对讲页面相关用例"""
    file_path = os.path.join(FILE_DIR, 'ip_talk_import.xls')
    # @pytest.mark.zls
    def test_add_ip_vocie(self, set_up_login):
        """验证添加2个对讲服务->编辑->删除任意对讲服务成功"""
        driver = set_up_login
        voice_page = IPVoicePage(driver)
        voice_page.open_ipvoice()
        # 添加2个对讲服务
        ip = ["192.168.0.144","192.168.0.121"]
        for i in ip:
            result = voice_page.add_voice_service(i)
            assert result == True

    # @pytest.mark.zls
    def test_edit_ip_voice(self,set_up_login):
        # 编辑第一个对讲服务
        driver = set_up_login
        voice_page = IPVoicePage(driver)
        voice_page.open_ipvoice()
        assert voice_page.edit_voice_service() == True

    # @pytest.mark.zls
    def test_del_ip_voice(self,set_up_login):
        driver = set_up_login
        voice_page = IPVoicePage(driver)
        voice_page.open_ipvoice()
        # 删除第一个对讲服务
        assert voice_page.del_voice_service() == True


    # @pytest.mark.zls
    def test_switch_org(self, set_up_login):
        """验证切换组织机构成功"""
        driver = set_up_login
        voice_page = IPVoicePage(driver)
        voice_page.open_ipvoice()
        result = voice_page.switch_org()
        url = driver.current_url
        text = (url.split('='))[-1]
        # url中含有中文，进行解码
        expected = parse.unquote(text)
        assert result == expected

    # @pytest.mark.zls
    def test_import_device(self, set_up_login):
        """验证导入设备成功"""
        driver = set_up_login
        voice_page = IPVoicePage(driver)
        voice_page.open_ipvoice()
        results = voice_page.import_device(self.file_path)
        assert results[0] == "2"
        assert results[1] == "200"
        assert results[2] == "200"