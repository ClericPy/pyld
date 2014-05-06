def huiwen(n):
    # 判断是不是回文数
    str(n)
    for i in range(len(n)):
        if n[i] != n[-1 - i]:
            return False
    return True
ll = []
for i in range(999, 100, -1):  # 放入列表便于求max
    for b in range(999, 100, -1):
        if huiwen(str(i * b)):
            ll.append(i * b)
print(max(ll))
