from cookiespool.db import RedisClient

conn = RedisClient('accounts', 'weibo')


# def set(account, sep='----'):
def set():
    # username, password = account.split(sep)

    username = '19181783661'
    password = 'puget123456'

    result = conn.set(username, password)
    print('账号', username, '密码', password)
    print('录入成功' if result else '录入失败')


def scan():
    print('请输入账号密码组, 输入exit退出读入')
    account = ['19181783661','puget123456']
    set()


if __name__ == '__main__':
    scan()
