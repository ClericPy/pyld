import urllib.request
import lxml.html
import re
import xlwt  # 该模块不支持65000以上行，如果需要，用openpyxl
该脚本会通过自动获取电脑报在线上面的最新内容并将标题、内容概括、
链接地址这三项存入Excel文件中，因为没使用openpyxl模块，所以只能存
为xls而不是xlsx那种可以存放超过65535行数据的格式，其实超过几十万行
存入数据库或者json里更好一些，超过几百万数据Excel2007格式也搞不定。

话说，这真是一个骗人的readme
