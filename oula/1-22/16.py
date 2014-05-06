# 就是把结果转换成字符串然后挨个提取出来再求和
ss = str(pow(2, 1000))
sum1 = 0
for i in ss:
    sum1 += int(i)
print(sum1)
