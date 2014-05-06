# codeing=utf-8
import urllib.request
import re
'''通过京东服务器查'''
url = 'http://item.jd.com/997951.html'
jdid = re.search(r'/(\d+)\.html', url).group(1)
# 上面获取了商品ID，下面就是把ID添加到京东那个查价格的json地址里
url = 'http://p.3.cn/prices/get?skuid=J_' + \
    str(jdid) + '&type=1&area=19_1601_51091&callback=cnp'
html = urllib.request.urlopen(url).read().decode('utf-8')
aa = re.search(r'"p":"(.*?)"', html).group(1)

print(aa)
