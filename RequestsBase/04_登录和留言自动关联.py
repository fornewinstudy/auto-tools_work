#!/usr/bin/env python3
# @Time : 2026/1/29 16:32
# @Author : 潘璐璐
import requests

s = requests.session()  # 定义一个请求会话，后续所有请求会话如果是基于该会话发送的请求，就可以实现自动关联
login_url = "http://www.mall.com/user.php"
login_data = {
    "username": "qqq",
    "password": "123456",
    "act": "act_login",
    "back_act": "http://www.mall.com/",
    "submit": "登 录",
}
login_resp = s.post(login_url, data=login_data)
assert "登录成功" in login_resp.text

leave_msg_url = "http://www.mall.com/user.php"
leave_msg_data = {
    "msg_type": "0",
    "msg_title": "留言",
    "msg_content": "留言",
    "act": "act_add_message",
}
leave_msg_resp = s.post(leave_msg_url, data=leave_msg_data)
assert "留言成功" in leave_msg_resp.text
