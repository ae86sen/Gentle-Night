

import pytest
import time

from alarm_manage_pages.seat_page import SeatPage

class TestSeat():
    """接警坐席页面相关用例"""

    # @pytest.mark.zls
    def test_open_org_tree(self, set_up_login):
        """验证展开所有组织机构成功"""
        driver = set_up_login
        seat_page = SeatPage(driver)
        seat_page.open_seat()
        result = seat_page.open_org_tree()
        time.sleep(5)
        assert result == True

    # @pytest.mark.zls
    def test_add_and_del_seat(self, set_up_login):
        """验证添加-删除坐席成功"""
        driver = set_up_login
        seat_page = SeatPage(driver)
        seat_page.open_seat()
        add_result = seat_page.add_seat()
        assert add_result == True
        del_result = seat_page.del_seat()
        assert del_result == False