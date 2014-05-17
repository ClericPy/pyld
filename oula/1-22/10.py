# 题目10：计算两百万以下所有质数的和。
from math import sqrt
# 导入求平方根的方法
# 求600851475143的最大质数因子是多少？


def zhishu(n):
    # 判断是不是质数
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

ss = 5

for a in range(5, 2000001):
    if a % 2 != 0 and a % 3 != 0 and zhishu(a):
        ss += a
print(ss)
