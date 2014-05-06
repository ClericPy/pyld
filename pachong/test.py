from bs4 import BeautifulSoup
import urllib.request

url = 'http://em.scnu.edu.cn/'
html = urllib.request.urlopen(url)
scode = html.read().decode('utf-8')

soup = BeautifulSoup(scode)

head = soup.find_all(id="kinMaxShow")

print(head)











