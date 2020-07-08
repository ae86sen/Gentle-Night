

import pytest
import time

from alarm_manage_pages.equiplink_page import EquipLinkPage

class TestEquipLink():
    """设备关联关系页面相关用例"""

    # @pytest.mark.zls
    def test_add_equip_link(self, set_up_login):
        """验证添加设备关联关系成功"""
        driver = set_up_login
        equip_link_page = EquipLinkPage(driver)
        equip_link_page.open_equiplink()
        result = equip_link_page.add_equip_link()
        assert result == "(3)"
        equip_link_page.clear()

