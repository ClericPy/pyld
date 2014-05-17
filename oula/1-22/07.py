from math import sqrt


def zhishu(n):  # 判断质数
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
aa = []
i = 2
while len(aa) != 10001:
    if zhishu(i):
        aa.append(i)
    i += 1
print(aa[-1])
