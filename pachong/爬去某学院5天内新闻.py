# codeing=utf-8
import urllib.request
import re
import time
import os

days=5

aa=time.time()


url = 'http://em.scnu.edu.cn/article/xueyuanxinwen/'
html = urllib.request.urlopen(url)
scode = html.read().decode('utf-8')

new = re.search(r'学院新闻.*?<span class="right">(.*?)<!--c_news-->', scode,flags=re.DOTALL).group(1).strip()
new = re.sub('<.*?>','',new)
new = re.sub('\s*','',new)
new = re.sub('\[','\n[',new)



url = 'http://em.scnu.edu.cn/article/xueyuantongzhi/'
html = urllib.request.urlopen(url)
scode = html.read().decode('utf-8')

notice = re.search(r'<a href="/article/xueyuantongzhi/zonghe/">更 多...</a></span>综合(.*?)<!--c_news-->', scode,flags=re.DOTALL).group(1).strip()
notice = re.sub('<.*?>','',notice)
notice = re.sub('\s*','',notice).replace('[推荐]','推荐:')
notice = re.sub('\[','\n[',notice)
notice = re.sub('更多\.\.\.','\n',notice)

result='学院新闻:\n'+new+'\n\n学院通知:\n'+notice+'\n'

li = re.findall(r'\[.*?\]', result)
li2=[]
for i in li:
	cc = i[1:11]
	bb = time.mktime(time.strptime(cc,"%Y-%m-%d"))
	dd = aa - bb
	if dd > days * 86400:
		li2.append(i)
for ii in li2:
	result = result.replace(ii,'~')
result = re.sub(r'~.*?\n','',result)
print(result)
os.system('pause')








