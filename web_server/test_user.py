"""
============================
Author:古一
Time:2020/8/14
E-mail:369799130@qq.com
============================
"""
from unittest import TestCase
from hello import db, User


class TestUser(TestCase):
    def test_user(self):
        user1 = User(username='listen3', password='123', email='listen3@163.com')
        db.session.add(user1)
        db.session.commit()
