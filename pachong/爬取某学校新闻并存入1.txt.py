# python3

import urllib.request
import lxml.html
import re

ye=22 #最大页码

xx=[]
for pp in range(1,ye+1):
    url = 'http://em.scnu.edu.cn/article/xueyuantongzhi/zonghe/list_120_%d.html'%(pp)
    html = urllib.request.urlopen(url)
    scode=html.read().decode('utf-8')
    doc = lxml.html.document_fromstring(scode)
    ss = doc.xpath("""//div[@class="c_news"]/ul/li/a/font/text()|//div[@class="c_news"]/ul/li/a/text()""")
    bb = doc.xpath("""//div[@class="c_news"]/ul/li/span/text()""")
    aa= list(zip(ss,bb))
    aa= [str(i).replace('(','').replace(')','').replace('\'','') for i in aa]
    xx+=aa

with open('1.txt','w') as f:
    for i in xx:
        f.write(i+'\n')