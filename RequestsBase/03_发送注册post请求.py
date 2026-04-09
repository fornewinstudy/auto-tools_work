#!/usr/bin/env python3
# @Time : 2026/1/29 15:23
# @Author : 潘璐璐
import requests


def register(count):
    register_url = "http://www.mall.com/user.php"
    register_data = {
        "username": f"abc{count}",
        "email": f"abc{count}@qq.com",
        "password": "123456",
        "confirm_password": "123456",
        "extend_field5": "15817252876",
        "agreement": "1",
        "act": "act_register",
        "back_act": "",
        "Submit": "同意协议并注册",
    }
    register_resp = requests.post(register_url, data=register_data)
    assert "注册成功" in register_resp.text


if __name__ == '__main__':
    for i in range(1, 1001):
        register(i)
