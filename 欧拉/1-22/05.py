ll = [2]
from math import sqrt


def zhishu(n):  # 判断质数
    for i in range(2, int(sqrt(n)) + 1):
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
for a in range(3, 21):  # 遇到一样的质因子就删了最后统一放进去
    if zhishu(a):
        ll.append(a)
    for c in zhiyinzi(a):
            if c in ll:
                ll.remove(c)
    ll = ll + zhiyinzi(a)
jieguo = 1
for e in ll:
    jieguo = jieguo * e
print(jieguo)
