"""
============================
Author:古一
Time:2020/7/5
E-mail:369799130@qq.com
============================
"""

import re

import pytest
import requests


@pytest.fixture(scope="session")
def test_token():
    res = None
    # 获取 token
    corpid = "wwa87b3203e469d9a3"
    corpsecret = "D9V_IFuwdEefp3Ix7U9ZpvpFQjs5Cdp1xLt2LrzDb3Y"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&"
                       f"corpsecret={corpsecret}")
    return res.json()["access_token"]


def test_get(userid, test_token):
    # 根据 user-id查询成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}")
    return res.json()


def test_create(userid, name, mobile, test_token):
    # 添加成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1],
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",
                        json=data
                        )
    return res.json()


def test_update(userid, name, mobile, test_token):
    # 更新成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",
                        json=data)
    return res.json()


def test_delete(userid, test_token):
    # 删除成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return res.json()


@pytest.mark.parametrize("userid, name, mobile", [("zhangsan12", "小黑", "13813210009")])
def test_all(userid, name, mobile, test_token):
    """组合测试"""
    # 添加成员
    assert test_create(userid, name, mobile, test_token)["errmsg"] == "created"
    assert test_get(userid,test_token)["name"] == name
    # 更新成员
    assert test_update(userid, "柯震东", mobile, test_token)["errmsg"] == "updated"
    assert test_get(userid,test_token)["name"] == "柯震东"
    # 删除成员
    assert test_delete(userid,test_token)['errmsg'] == "deleted"
    assert test_get(userid,test_token)['errcode'] == 60111