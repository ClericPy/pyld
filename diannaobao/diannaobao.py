# python3
import urllib.request
import lxml.html
import re
import xlwt  # 该模块不支持65000以上行，如果需要，用openpyxl

'''
该脚本会通过自动获取电脑报在线上面的最新内容并将标题、内容概括、
链接地址这三项存入Excel文件中，因为没使用openpyxl模块，所以只能存
为xls而不是xlsx那种可以存放超过65535行数据的格式，其实超过几十万行
存入数据库或者json里更好一些，超过几百万数据Excel2007格式也搞不定。

'''


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


def geturl():
    gg = yuandaima('http://www.icpcw.com/Newspaper/Hot')
    uuu = 'http://www.icpcw.com' + \
        getxpath('//div[@class="j_ywnav"]/ul/li[2]/a/@href', gg)[0]
    return uuu


if __name__ == '__main__':
    url = geturl()
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

    contents = qukongge(contents)

    # ff = list(zip(titles, contents, hrefs))

    # ff = ['\t'.join(aa) for aa in ff]
    # print(ff)

    wbk = xlwt.Workbook()
    sheet1 = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)

    i = 0
    for _ in titles:
        sheet1.write(i, 0, _)
        i += 1
    i = 0
    for _ in contents:
        sheet1.write(i, 1, _)
        i += 1
    i = 0
    for _ in hrefs:
        sheet1.write(i, 2, _)
        i += 1
    wbk.save('test.xls')
