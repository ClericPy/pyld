# codeing=utf-8
import urllib.request
import re
import random

# iplist=['5.98.86.141:8080','24.172.34.114:8181','27.145.145.105:8080']

list1 = ['百度', '清明', '锄禾', '期待', '钓鱼岛', 'django']
for i in list1:
    # ip=random.choice(iplist)

    gjc = urllib.request.quote(i)
    url = 'http://suggestion.baidu.com/su?wd=' + gjc + \
        '&json=1&p=3&sid=&cb=jQuery110205425511478908079_1396251136074&_=1396251136078'
    headers1 = {'GET': url,
                'Host': "suggestion.baidu.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:28.0) Gecko/20100101 Firefox/28.0",
                'Referer': "http://www.baidu.com/"}

    # proxy_support=urllib.request.ProxyHandler({'http':'http://'+ip})
    # opener=urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)

    req = urllib.request.Request(url, headers=headers1)
    html = urllib.request.urlopen(req).read().decode('gbk')
    ss = re.findall('\[.*\]', html)
    print(ss[0].strip('[').strip(']').replace('"', '').split(','))
