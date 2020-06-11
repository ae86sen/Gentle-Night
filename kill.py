"""
============================
Author:古一
Time:2020/6/1
E-mail:369799130@qq.com
============================
"""
import requests

#
#
# def doc(st):
#     def retry_conncet(func):
#
#         def wrapper(*args,**kwargs):
#             n = 0
#             while n<=5:
#                 try:
#                     func(*args,**kwargs)
#                     print("连接成功")
#                 except Exception as e:
#                     n += 1
#                     print(f"连接失败第{n}次")
#                     continue
#                 else:
#                     print(st)
#                     break
#         return wrapper
#     return retry_conncet
#
#
#
#
#
# @doc('三层哟西')
# def request_url(url):
#     return requests.get(url)
#
# url = r"http://www.baidu.com"
#
# request_url(url)

data = [{"mob": "131", "pwd": "123456"},
        {"mob": "132", "pwd": "123456"}]
def register():
    names = input("请输入账号：")
    users = [x['mob'] for x in data]
        # print(i.get("mob")) # 遍历得到的mob为131 和132
    if names not in  users:
        pwd1 = input("请输入密码：")
        pwd2 = input("请确认密码：")
        if pwd2 == pwd1:
            print("注册成功")
        else:
            print("两次密码不一致")
    else:
        print("账号已被注册")

register()
