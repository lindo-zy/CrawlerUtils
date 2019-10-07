import requests

from cookiespool.db import AccountRedisClient

conn = AccountRedisClient(name='weibo')


def scan():
    # 账号
    accounts = [{"username": '19181783661', "password": "puget123456"},
                {"username": '19181783661', "password": "puget123456"}]

    for acount in accounts:
        username = acount.get('username')
        password = acount.get('password')
        result = conn.set(username, password)
        print('账号', username, '密码', password)
        print('录入成功' if result else '录入失败')


if __name__ == '__main__':
    scan()
