"""
============================
Author:古一
Time:2020/8/14
E-mail:369799130@qq.com
============================
"""
from unittest import TestCase
from hello import db,Cases

class TestTestCases(TestCase):
    def test_create(self):
        db.create_all()

    def test_get(self):
        user1 = Cases(case_title='删除用户',case_precondition='登录',case_steps='xxx',case_expected='删除成功')
        db.session.add(user1)
        db.session.commit()
