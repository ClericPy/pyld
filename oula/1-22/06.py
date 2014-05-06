# 题目6：平方和与和平方的差是多少？
def pingfanghe():
    ss = 0
    for a in range(1, 101):
        ss += a ** 2
    return ss
print(sum(range(1, 101)) ** 2 - pingfanghe())
