#!/usr/bin/env python3
# @Time : 2026/1/30 15:29
# @Author : 潘璐璐
import requests
from ApiFramework.conf.config import LoginUrl


def get_cookie(user="qqq", pwd="123456"):
    url = LoginUrl
    login_data = {
        "username": user,
        "password": pwd,
        "act": "act_login",
        "back_act": "http://www.mall.com/goods.php?id=30",
        "submit": "登 录"
    }
    resp = requests.post(url, data=login_data)
    assert "登录成功" in resp.text
    return resp.cookies


if __name__ == '__main__':
    print(get_cookie())
