#!/usr/bin/env python3
# @Time : 2026/1/29 17:37
# @Author : 潘璐璐
import requests

login_url = "http://appapi.fecshop.com/v1/account/login"
login_json = {
    "username": "admin",
    "password": "admin123"
}
login_resp = requests.post(login_url,json=login_json)
print(login_resp.text)