#!/usr/bin/env python3
# @Time : 2026/1/29 15:15
# @Author : 潘璐璐
import requests

login_url = "http://www.mall.com/user.php"
login_data = {
    "username": "qqq",
    "password": "123456",
    "act": "act_login",
    "back_act": "http://www.mall.com/goods.php?id=30",
    "submit": "登 录",
}
login_resp = requests.post(login_url, data=login_data)
# 方法一：通过if判断来断言
if "登录成功" in login_resp.text:
    print("断言成功")
else:
    print("断言失败")

# 方法二：使用python提供的assert关键字断言
assert "登录成功" in login_resp.text
