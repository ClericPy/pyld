# codeing=utf-8
import urllib.request
import re
import time
import json

timestamp_ = time.time()
url = 'http://www.vitacost.com/muscle-pharm-assault-fruit-punch-0-96-lbs-1'

headers1={'GET':url,
    'Host':"www.vitacost.com",
    'User-Agent':"Mozilla/5.0 (Windows NT 6.2; rv:28.0) Gecko/20100101 Firefox/28.0",
    'Referer':url}
req=urllib.request.Request(url,headers=headers1)

html = urllib.request.urlopen(req)
scode = html.read().decode('utf-8')
status_ = 1 if html.getcode()==200 else 0
Star = re.search(r'<span class="average">(.*?)</span>', scode, flags=re.DOTALL).group(1).strip()
title_= re.search(r'<head><title>(.*?)--', scode, flags=re.DOTALL).group(1).strip()
source_url = url
pid_ = re.search(r'product details:(.*?)";', scode,
                 flags=re.DOTALL).group(1).strip()

id_type = re.search(r'<div>(\w*) #: ' + pid_, scode,
                    flags=re.DOTALL).group(1).strip()
brand_ = re.search(r'var vPBrandName = \'(.*?)\'', scode,
                   flags=re.DOTALL).group(1).strip()
intro_ = re.search(r'!-- description -->(.*?)<!-- /description -->', scode,
                   flags=re.DOTALL).group(1).strip()
intro_ = re.sub('<.*?>', '', intro_)
intro_ = re.sub('\s{2}', ' ', intro_)


category_ = re.search(r'<div class="cttHdr cttHdrBr">(.*?)</div>', scode,flags=re.DOTALL).group(1).strip()
category_ = re.sub('<.*?>','>',category_).replace('>>',' >')

currency_ = re.search(r'Retail price: (.{1})', scode,flags=re.DOTALL).group(1)


jsdic = {"status_":status_,"source_url":source_url,"time":timestamp_,"Star":Star}
jsjs = json.dumps(jsdic, indent=4)
with open('result.json','w',encoding='utf-8') as f:
	f.write(jsjs)
