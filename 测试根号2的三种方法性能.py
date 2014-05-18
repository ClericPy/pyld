import timeit
t1=timeit.timeit('i=math.sqrt(2)','import math')
t2=timeit.timeit('a=2**0.5')
t3=timeit.timeit('b=pow(2,0.5)')
print(t1);print(t2);print(t3)
