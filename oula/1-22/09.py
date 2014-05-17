# 题目9：找出唯一的满足a + b + c = 1000的毕达哥拉斯三元组{a, b, c}。
for a in range(1, 501):
    for b in range(1, 501):
        if a ** 2 + b ** 2 == (1000 - a - b) ** 2 and a < b:
            print('a:', a, '\n b:', b, '\n c:',
                  1000 - a - b, '\n abc:', a * b * (1000 - a - b))
            break
            break
'''因为a2+b2=c2
→(a+b)2=c2+2ab>c2
→a+b>c
→a+b>1000-a-b
→a+b>500
→a<b<c<500
'''
