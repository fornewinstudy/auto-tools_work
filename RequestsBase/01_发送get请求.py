#!/usr/bin/env python3
# @Time : 2026/1/29 14:08
# @Author : 潘璐璐
import requests

url = "http://www.mall.com/"  # 访问的网址
resp = requests.get(url)  # 调用requests模块下的get方法发送get无参请求
print(resp.status_code)  # 查看接口返回的状态码
print(resp.text)  # 查看接口返回的响应文本，返回数据类型是字符串
print(resp.content)  # 查看接口返回的响应内容，返回数据类型是bytes
print(resp.content.decode("utf-8"))  # 将字节转成字符
print(resp.elapsed)  # 查看接口的响应时间
print(resp.cookies)  # 查看接口返回的cookies信息
print(resp.headers)  # 查看接口返回的响应头信息

url1 = "http://www.mall.com/goods.php"  # 访问的网址
param = {"id": 30}  # 在requests中，对于参数我们需要以字典的形式传入
resp1 = requests.get(url1, params=param)  # 调用requests模块下的get方法发送get有参请求
print(resp1.text)

# get请求参数是在url中，因此我们也可以直接将参数与接口地址进行拼接
url2 = "http://www.mall.com/goods.php?id=30"
resp2 = requests.get(url2)  # 由于参数直接拼接到了url2中，发送请求时就不用定义参数
print(resp2.text)
