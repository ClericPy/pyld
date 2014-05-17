#暴力算法
jiecheng=1
for i in range(1,101):
	jiecheng*=i
ss=str(jiecheng)
jieguo=0
for s in ss:
	jieguo+=int(s)
print(jieguo)