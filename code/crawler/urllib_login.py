#conding=utf-8

import urllib.request
import urllib.parse

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'SINAGLOBAL=7457543685746.846.1526920772568; wvr=6; UOR=,,login.sina.com.cn; wb_timefeed_3687124030=1; YF-Ugrow-G0=ea90f703b7694b74b62d38420b5273df; SSOLoginState=1528206850; YF-V5-G0=d8809959b4934ec568534d2b6c204def; _s_tentry=-; Apache=622883149122.5195.1528206859030; ULV=1528206859072:3:2:2:622883149122.5195.1528206859030:1528125761390; YF-Page-G0=23b9d9eac864b0d725a27007679967df; TC-Page-G0=e2379342ceb6c9c8726a496a5565689e; TC-V5-G0=784f6a787212ec9cddcc6f4608a78097; TC-Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e; SCF=AqS7bk4TwnIwE7Eyj9Ji-OrySOwCe41Gefugpqei7rFX7GIcD1_IETzgKRQtuYAUweGhNb1hrmoCYPWVTtGiTsw.; SUB=_2A252E5sGDeRhGeVI41UQ8irMyDyIHXVVaIvOrDV8PUNbmtANLVjNkW9NTy56Hk0wKG5Nf_qr1tnxIDNQ8x4aZd6G; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFhmhV1ESn8L163J.MghHgp5JpX5KMhUgL.Foec1hMpeoB7e052dJLoI79iKgHLU8Yt; SUHB=0nluWsLnIoAV1O; ALF=1559830229; cross_origin_proto=SSL; wb_cmtLike_3687124030=1',
    'Host': 'weibo.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 QQBrowser/4.3.4986.400'
}

url = 'https://weibo.com/comment/inbox'

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
