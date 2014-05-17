#先读取出来然后转换成列表，用sort排序
with open('names.txt') as f:
	ll=f.read().replace('"','').split(',')
def aaa(zimu):
	ss=0
	alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for x in zimu:
		ss=ss+alpha.index(x)+1
	return ss

ll.sort()
jieguo=0
for i, item in enumerate(ll):#enumerate真心很好用啊
	jieguo+=(i+1)*aaa(item)

print(jieguo)