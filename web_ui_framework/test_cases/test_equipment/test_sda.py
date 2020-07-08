
import os
import pytest
import time

from equipment_pages.sda_page import SdaPage
from common.constants import FILE_DIR
file_path = os.path.join(FILE_DIR,"zongmu_host.json")

class TestSda():
    """虚拟主机类型页面相关用例"""

    # @pytest.mark.skip
    # @pytest.mark.zls
    def test_upload_sda_file(self,master,set_up_login):
        """验证上传SDE文件成功"""
        driver_master = master
        sda_page_m = SdaPage(driver_master)
        sda_page_m.open_master_sda()
        sda_page_m.upload_sde_file(file_path)
        time.sleep(330)
        driver = set_up_login
        sda_page = SdaPage(driver)
        sda_page.open_sda()
        result = sda_page.get_info()
        assert result == True
        # 添加完后删除
        # sda_page.del_sde_file()