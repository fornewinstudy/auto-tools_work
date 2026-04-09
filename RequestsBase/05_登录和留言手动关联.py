#!/usr/bin/env python3
# @Time : 2026/1/29 16:40
# @Author : 潘璐璐
import requests

login_url = "http://www.mall.com/user.php"
login_data = {
    "username": "qqq",
    "password": "123456",
    "act": "act_login",
    "back_act": "http://www.mall.com/",
    "submit": "登 录",
}
login_resp = requests.post(login_url, data=login_data)
cookie = login_resp.cookies
assert "登录成功" in login_resp.text

leave_msg_url = "http://www.mall.com/user.php"
leave_msg_data = {
    "msg_type": "0",
    "msg_title": "留言666",
    "msg_content": "留言666",
    "act": "act_add_message",
}
leave_msg_resp = requests.post(leave_msg_url, data=leave_msg_data, cookies=cookie)
assert "留言成功" in leave_msg_resp.text
