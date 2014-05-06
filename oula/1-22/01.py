a = 0
# 求3或5的倍数的和
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        a += i
print(a)
