def ss(aa):
    count = 1
    while aa != 1:
        count += 1
        if aa % 2 == 0:
            aa = aa / 2
        else:
            aa = aa * 3 + 1
    return count
jieguo = 0
a = 1
while a < 1000000:
    if ss(a) > jieguo:
        jieguo = ss(a)
        print(a, jieguo)
    a += 1
