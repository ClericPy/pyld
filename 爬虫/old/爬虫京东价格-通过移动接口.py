# codeing=utf-8
import urllib.request
import re
# 通过京东移动接口
url = 'http://item.jd.com/997951.html'
jdid = re.search(r'/(\d+)\.html', url).group(1)

url = 'http://m.jd.com/product/' + str(jdid) + '.html'
html = urllib.request.urlopen(url).read().decode('utf-8')
aa = re.findall(
    r'<font color="red" style="font-family:Arial;font-weight:bold;font-size:18px">&.*</font>',
    html)[0]

aa = re.findall(r'\d+\.\d+', aa)
print(aa[0])
