# codeing=utf-8
import urllib.request
import re



url = 'http://hi.baidu.com/lidongone/item/391213077948d9e0fe240d70'
html = urllib.request.urlopen(url)
scode = html.read().decode('utf-8')

aa = re.search(r'canshu1kaishi-(.*?)-canshu1jieshu', scode).group(1)
bb = re.search(r'canshu2kaishi-(.*?)-canshu2jieshu', scode).group(1)


print(aa, bb)
