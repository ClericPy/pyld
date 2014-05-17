# 题目12：第一个拥有超过500个约数的三角形数是多少？
from math import sqrt


def zhiyinzi(m):  # 分解出质因子到列表中
    aa = 2
    zyz = []
    while aa < m + 1:
        if m % aa == 0 and zhishu(aa):
            zyz.append(aa)
            m = m / aa
            continue
        else:
            aa += 1
    return zyz


def zhishu(n):  # 判断质数
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def ysgs(n):
    zys = zhiyinzi(n)
    geshu = []
    ji = 1
    for ji in zys:
        while ji < n:
            for i in zys:
                ji *= i

    return len(geshu) + len(zhiyinzi(n)) + 2


def sanjiaoxing(n):
    return n * (n + 1) / 2
for i in range(1, 100):
    print('ysgs', i, ysgs(sanjiaoxing(i)), ysgs(i / 2) * ysgs(i + 1))
