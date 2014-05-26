# -*- coding: utf-8 -*-
ll = [2]


def zhishu(n):  # 判断质数
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


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
print(zhiyinzi(987654))
a = 1
b = 19
