# python3
import urllib.request
import lxml.html
import re


def yuandaima(ss):
    url = ss
    headers1 = {'GET': url,
                'Host': "www.icpcw.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:28.0) Gecko/20100101 Firefox/28.0",
                'Referer': url}
    req = urllib.request.Request(url, headers=headers1)
    html = urllib.request.urlopen(req)
    scode = html.read().decode('utf-8', 'ignore')
    return scode


def panduan(ss):
    bb = getxpath(
        '''//div[@class="pager"]/span[@class="effective"]/a/@href''',
        ss)
    bb = list(set(bb))
    bb = ['http://www.icpcw.com' + i for i in bb]
    return bb


def qukuohao(aa):
    bb = [re.sub('<.*?>', '', _) for _ in aa]
    return bb


def qukongge(aa):
    bb = [re.sub('\s', '', _) for _ in aa]
    return bb


def getxpath(ss, daima):
    doc = lxml.html.document_fromstring(daima)
    aa = doc.xpath(ss)
    return aa

if __name__ == '__main__':
    url = 'http://www.icpcw.com/Newspaper/117/'
    scode = yuandaima(url)
    if panduan(scode):
        urls = panduan(scode) + [url]
    else:
        urls = [url]
    titles, contents, hrefs = [], [], []
    for uu in urls:
        yy = yuandaima(uu)
        title = getxpath('''//td[@class="sub3titfc"]/a/text()''', yy)
        content = getxpath('''//td[@class="sub3fc2"]/text()[2]''', yy)
        href = getxpath('''//td[@class="sub3titfc"]/a/@href''', yy)
        href = ['http://www.icpcw.com' + i for i in href]
        titles += title
        contents += content
        hrefs += href

    contents=qukongge(contents)

    ff = list(zip(titles, contents, hrefs))
<<<<<<< HEAD:自动爬取电脑报在线/diannaobao.py
    # ff = [str(aa) for aa in ff]
    print(str(ff[0]))
=======
    print(ff)
>>>>>>> 973ac24e93630b227bb710619d3e92bcddd658f7:diannaobao.py








    # with open('1.txt', 'w',encoding='utf-8') as f:
    #     for i in ff:
    #         f.write(str(i) + '\n\n')
