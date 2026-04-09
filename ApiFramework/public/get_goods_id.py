#!/usr/bin/env python3
# @Time : 2026/1/31 11:16
# @Author : 潘璐璐
import requests
from ApiFramework.conf.config import QueryGoodsUrl
import re
import random

def get_gid(kw="水果"):
    url,query_data = QueryGoodsUrl,{"keywords":kw,"dataBi":"k1"}
    resp = requests.get(url,params=query_data)
    pattern = r'href="goods\.php\?id=(\d+)"'    # 书写正则表达式
    matches = re.findall(pattern,resp.text) # 通过findall方法在接口返回的字符串中提权正则表达式的内容
    return random.choice(matches)


if __name__ == '__main__':
    print(get_gid())
