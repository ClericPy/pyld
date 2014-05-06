#! python3
# -*- coding: utf-8 -*-
import ctypes
import time
import re
import sys
import os
ahk = ctypes.cdll.AutoHotkey  # load AutoHotkey
ahk.ahktextdll("")
while not ahk.ahkReady():
    time.sleep(0.01)
goahk = ahk.ahkExec

'''
C:\Program Files\UXin\UXinClient.exe这一句是有信文件路径
用法是先在numlist.ini文件里放入帐号密码，一行表示一个帐号，
逗号隔开帐号与密码，最后结果会生成到result.txt里面
如果运行失败，那问题很可能是分辨率造成的找图失败，
需要重新抓那几个png图，本实例仅供参考，失败很正常吧
'''

def checkit():
    with open('result.txt', 'r') as f:
        xx = f.readlines()[-1]
    with open('result.txt', 'r') as f:
        yiqiandaoresult = f.read()
    todayday = time.strftime("%Y-%m-%d", time.localtime())
    if xx.startswith(todayday):
        print('已签到过')
        print(yiqiandaoresult)
        os.system('pause')
        sys.exit()
    return

if os.path.exists('result.txt'):
    checkit()


goahk(r'''
	F2::
	pause
	return
	F3::
	WinClose 有信
	WinClose 有信2013
	Process, Close,python.exe
	return
	''')


def zhaotu(a, b, c, d, e):
    goahk('aa=' + str(a))
    goahk('bb=' + str(b))
    goahk('cc=' + str(c))
    goahk('dd=' + str(d))
    goahk('ee=' + str(e))

    mingling = r'''
	Loop
	{
	Sleep 200
	ImageSearch,x,y,%aa%,%bb%,%cc%,%dd%,%ee%.png
	if ErrorLevel
		continue
	else
	    break
		}
	'''
    goahk(mingling)

    xx = ctypes.cast(ahk.ahkgetvar("x", 0), ctypes.c_wchar_p).value
    yy = ctypes.cast(ahk.ahkgetvar("y", 0), ctypes.c_wchar_p).value

    zb = xx + ',' + yy
    return zb


def dianji(a, b, c, d, e):
    goahk('aa=' + str(a))
    goahk('bb=' + str(b))
    goahk('cc=' + str(c))
    goahk('dd=' + str(d))
    goahk('ee=' + str(e))

    mingling = r'''
	Loop
	{
	Sleep 200
	ImageSearch,x,y,%aa%,%bb%,%cc%,%dd%,%ee%.png
	if ErrorLevel
		continue
	else
	    break
		}
	Click %x%,%y%
	'''
    goahk(mingling)


def qiandao(a, b):
    a = str(a)
    b = str(b)
    goahk('zhanghao=' + a)
    goahk('mima=' + b)
    goahk(r'''
	run C:\Program Files\UXin\UXinClient.exe
	WinWait 有信
	WinActivate 有信
	Loop
	{
	Sleep 200
	ImageSearch,x,y,38,42,226,171,denglu.png
	if ErrorLevel
		continue
	else
	    break
		}
	Sleep 100
	Click 100,213
	Send ^a%zhanghao%{Tab}^a%mima%{Enter}
	WinWait 有信2013
	WinActivate 有信2013
	''')
    dianji(126, 81, 181, 109, 'zhuanhuafei')
    dianji(708, 113, 817, 163, 'dianwoqiandao')
    goahk(r'''
		sleep 200
		Loop
		{
		Sleep 200
		ImageSearch,x,y,383,105,613,166,ninjintian.png
		if ErrorLevel{
			Click 760,138
			continue
			}
		else break
			}''')
    goahk(r'''
		clipboard =
		Click 387,123,0
		Click down
		Click 619,123,0
		Click up
		Send ^c
		ClipWait
		yiqiandao=%Clipboard%
		sleep 100
		Click 592,42
		''')
    x = ctypes.cast(ahk.ahkgetvar("yiqiandao", 0), ctypes.c_wchar_p).value
    zhaotu(610, 126, 725, 157, 'ketonghua')
    goahk(r'''
		Click 637,167,0
		Click down
		Click 740,168,0
		Click up
		clipboard =
		Send ^c
		ClipWait
		shengyu=%Clipboard%
		WinClose 有信
		WinClose 有信2013
		sleep 500
		''')

    y = str(ctypes.cast(ahk.ahkgetvar("shengyu", 0), ctypes.c_wchar_p).value)
    x = re.sub('\D', '', x)
    print(a + ':已签到' + x + '分钟,还剩余' + y + '\n')
    return a + ':已签到' + x + '分钟,还剩余' + y + '\n'

start = time.clock()

with open('numlist.ini', 'r') as f:
    numlist = f.readlines()

numlist = [re.sub('\s', '', i) for i in numlist]
numlist = [re.split('\W', ii) for ii in numlist]


result = ''
for i in numlist:
    result += qiandao(i[0], i[1])

end = time.clock()
jishi = '\n本次签到程序耗费' + str(round(end - start)) + '秒\n'
result += jishi
result += time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open('result.txt', 'w') as f:
    f.write(result)
print(result)
os.system('pause')
sys.exit()
