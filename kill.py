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
li = ["{'a':1,'b':2}","[11,22,33]"]
li1 = [eval(i) for i in li]
print(li1)

li2 = [i*5 for i in range(0,11)]
print(li2)

li3 = [f"page{i}" for i in range(1,11)]
print(li3)

Names = ["python","c","c++","java","unittest","djagon","flask"]
li4 = [i for i in Names if len(i)>4]
li5 = [i if len(i)>4 else None for i in Names]
print(li5)
