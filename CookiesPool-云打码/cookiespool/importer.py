import requests

from cookiespool.db import AccountRedisClient

conn = AccountRedisClient(name='weibo')


def set():
    # username, password = account.split(sep)
    username = '19181783661'
    password = 'puget123456'
    result = conn.set(username, password)
    print('账号', username, '密码', password)
    print('录入成功' if result else '录入失败')


def scan():
    print('请输入账号密码组, 输入exit退出读入')
    # while True:
    #     account = input()
    #     if account == 'exit':
    #         break
    set()


if __name__ == '__main__':
    scan()
