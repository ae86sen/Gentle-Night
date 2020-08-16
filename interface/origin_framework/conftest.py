"""
============================
Author:古一
Time:2020/7/3
E-mail:369799130@qq.com
============================
"""
import pytest
import requests


@pytest.fixture()
def get_token():
    corpid = 'wwa87b3203e469d9a3'
    corpsecret = 'D9V_IFuwdEefp3Ix7U9ZpvpFQjs5Cdp1xLt2LrzDb3Y'
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    token = res.json()["access_token"]
    yield token
    pass