"""
============================
Author:古一
Time:2020/7/3
E-mail:369799130@qq.com
============================
"""
import jsonpath
import requests


class TestDemo:
    url = r"https://qyapi.weixin.qq.com/cgi-bin/department"

    def test_add_dep(self, get_token):
        """添加部门"""
        token = get_token
        datas = {
            "name": "调研部",
            "parentid": 1,
        }
        res = requests.post(self.url + f"/create?access_token={token}", json=datas)
        print(res.json())

    def test_edit_dep(self, get_token):
        """更新部门"""
        token = get_token
        datas = {
            "id": 9,
            "name": "安全部",
            "parentid": 1
        }
        res = requests.post(
            self.url + f"/create?access_token={token}",
            json=datas)
        print(res.json())

    def test_del_dep(self, get_token):
        """删除部门"""
        token = get_token
        res = requests.get(
            self.url + f"/delete?access_token={token}&id=9")
        print(res.json())

    def test_get_dep(self, get_token):
        """获取所有部门"""
        token = get_token
        res = requests.get(self.url + f"/list?access_token={token}")
        print(res.json())
