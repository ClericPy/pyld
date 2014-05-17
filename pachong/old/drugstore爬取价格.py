# codeing=utf-8
import urllib.request
import re

url = 'http://www.drugstore.com/halo-purely-for-pets-liv-a-littles-protein-treats-white-meat-chicken/qxp86856?catid=296447'
html = urllib.request.urlopen(url).read().decode('utf-8')
html = re.search(r'suggested:</a>&nbsp;<s>\$(.*)</s></span>', html).group(1)
print(html)