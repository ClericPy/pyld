# codeing=utf-8
import urllib.request
import re

url = 'http://m.jd.com/product/937680.html'


html = urllib.request.urlopen(url).read().decode('utf-8')
aa=re.findall(r'<font color="red" style="font-family:Arial;font-weight:bold;font-size:18px">&.*</font>', html)[0]

aa=re.findall(r'\d+\.\d+', aa)
print(aa[0])