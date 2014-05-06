def feb(n):  # 斐波那契数列递归
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return feb(n - 1) + feb(n - 2)
sum1 = 0
i = 1
while feb(i) <= 4000000:
    # 考虑斐波那契数列中数值不超过4百万的项，找出这些项中值为偶数的项之和。
    if feb(i) % 2 == 0:
        sum1 += feb(i)
    i += 1
print(sum1)
