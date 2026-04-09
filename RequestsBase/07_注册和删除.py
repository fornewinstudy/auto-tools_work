#!/usr/bin/env python3
# @Time : 2026/1/29 17:28
# @Author : 潘璐璐
import pymysql
import requests


def register():
    register_url = "http://www.mall.com/user.php"
    register_data = {
        "username": "abc",
        "email": "abc@qq.com",
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


def conn_mysql(sql):
    # 连接MySQL的基本信息
    db = pymysql.connect(host='127.0.0.1',
                         user='mall',
                         password='123456',
                         port=3306,
                         database="mall"
                         )
    # 使用cursor方法创建一个游标对象
    cursor = db.cursor()
    # 调用execute方法执行sql语句
    cursor.execute(sql)
    # 使用fetchall方法获取查询结果的所有数据
    # data = cursor.fetchall()
    db.close()  # 关闭数据库的连接


if __name__ == '__main__':
    del_sql = 'delete from ecs_users where user_name="abc"'
    conn_mysql(del_sql)
    register()
