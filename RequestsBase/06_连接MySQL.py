#!/usr/bin/env python3
# @Time : 2026/1/29 17:17
# @Author : 潘璐璐
import pymysql


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
    # query_sql = 'select * from ecs_users where user_name like "qqq%"'
    # 调用execute方法执行sql语句
    cursor.execute(sql)
    # 使用fetchall方法获取查询结果的所有数据
    data = cursor.fetchall()
    print(data)
    db.close()  # 关闭数据库的连接


if __name__ == '__main__':
    conn_mysql('select * from ecs_users where user_name like "qqq%"')
