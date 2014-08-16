def fib(n):
    """返回小于指定值的斐波那契数列偶数和"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

print(sum([aa for aa in fib(4000000) if aa % 2 == 0]))
# 4613732
#[Finished in 0.4s]
