"""
============================
Author:古一
Time:2020/6/23
E-mail:369799130@qq.com
============================
"""
import requests
from requests.auth import HTTPBasicAuth


class TestDemo:

    def test_demo(self):
        r = requests.get("http://httpbin.testing-studio.com/basic-auth/admin/admin",
                         auth=HTTPBasicAuth("admin", "admin"))
        print(r.text)

    def test_post(self):
        datas = {
            "name": "mark",
            "age": 18
        }
        r = requests.post("http://httpbin.testing-studio.com/post", json=datas)
        print(r.text)
        print(r.json())
