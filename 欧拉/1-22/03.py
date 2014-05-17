from math import sqrt
# 导入求平方根的方法
# 求600851475143的最大质数因子是多少？


def zhishu(n):
    # 判断是不是质数
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = 600851475143
b = 600851475143
i = 2
while i <= b:
    if n % i == 0 and zhishu(i):
        b = b / i  # b的长度越变越小利于运算
        print(i)
        if zhishu(n / i):
            print(n / i)
            break
    i = i + 1  # i越来越靠近b
# 最后结果找个最大的就有了
