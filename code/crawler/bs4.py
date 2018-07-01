#conding=utf-8

from bs4 import BeautifulSoup
import requests
import time

def captchaMethod(captcha_data):
    with open('captcha.jpg', 'wb') as f:
        f.write(captcha_data)
    return input('请输入验证码：')     

def getLoginZhihu():
    # 构建Session对象，保存cookie值
    sess = requests.Session()

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 QQBrowser/4.3.4986.400'
    }

    html = sess.post('https://www.zhihu.com/#sigin', headers=headers).text
    bs = BeautifulSoup(html, 'lxml')
    _xsrf = bs.find('input', attrs={'name': '_xsrf'}).get('value')

    captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
    captcha = sess.get(captcha_url, headers=headers).content

    # 获取验证码文字
    text = captchaMethod(captcha)

    data = {
        '_xsrf': _xsrf,
        'email': '123636374@qq.com',
        'password': 'ALARMCHIME',
        'captcha': text
    }
    # 登录 获取cookie
    res = sess.post('https://www.zhihu.com/login/email', data=data, headers=headers).text

    res = sess.get('https://www.zhihu.com/people/', headers=headers)

if __name__ == '__main__':
    getLoginZhihu()
