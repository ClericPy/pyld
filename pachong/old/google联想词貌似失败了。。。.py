# codeing=utf-8
import urllib.request


word = '哈哈哈'

gjc = urllib.request.quote(word)
url = r'https://www.google.com.hk/complete/search?client=hp&hl=zh-CN&tok=bFXyqQQigK4UbwnsMyJ4lg&cp=2&gs_id=7c&q=%E9%98%BF%E6%96%AF&xhr=t'



aa,bb= urllib.request.urlretrieve(url)




print(type(aa))
