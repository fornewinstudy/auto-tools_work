#!/usr/bin/env python3
# @Time : 2026/1/31 16:17
# @Author : 潘璐璐
import requests
from ApiFramework.conf.config import FecshopLoginUrl


def get_token(user='admin', pwd="admin123"):
    url, json_data = FecshopLoginUrl, {"username": user, "password": pwd}
    resp = requests.post(url, json=json_data).json()
    return {"access-token": resp["access-token"]}


if __name__ == '__main__':
    print(get_token())
