"""
============================
Author:古一
Time:2020/7/5
E-mail:369799130@qq.com
============================
"""
import random
import re

import pytest
import requests


@pytest.fixture(scope="session")
def test_token():
    # 获取 token
    corpid = "wwa87b3203e469d9a3"
    corpsecret = "D9V_IFuwdEefp3Ix7U9ZpttU-QOv4OgBM8CwHZTOKmI"
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


# def test_create_data():
#     data = [(str(random.randint(1000, 9999)), "吴亦凡", str(random.randint(13880840000, 13880849999))) for x in range(10)]
#     return data
def test_create_data():
    data = [("admin" + str(x), "zhangsan", "138%08d" % x) for x in range(10)]
    return data


@pytest.mark.parametrize("userid, name, mobile", test_create_data())
def test_all(userid, name, mobile, test_token):
    """组合测试"""
    # 添加成员
    try:
        assert test_create(userid, name, mobile, test_token)["errmsg"] == "created"
    except AssertionError as e:
        # print("错误："+ e.__str__())
        if "mobile existed" in e.__str__():
            # 正则取出存在的用户id， mobile existed:zhangsan12
            re_userid = re.findall(":(.*?)'", e.__str__())[0]
            # 将存在的用户删除
            assert test_delete(re_userid, test_token)['errmsg'] == "deleted"
            # 再判断
            assert test_get(re_userid, test_token)['errcode'] == 60111
            # 再重新创建该用户
            assert test_create(userid, name, mobile, test_token)["errmsg"] == "created"
    assert test_get(userid, test_token)["name"] == name
    # 更新成员
    assert test_update(userid, "柯震西", mobile, test_token)["errmsg"] == "updated"
    assert test_get(userid, test_token)["name"] == "柯震西"
    # 删除成员
    assert test_delete(userid, test_token)['errmsg'] == "deleted"
    assert test_get(userid, test_token)['errcode'] == 60111
