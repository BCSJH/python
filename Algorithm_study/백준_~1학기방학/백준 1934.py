def re(x, y):
    while y is not 0:
        r = x%y
        x = y
        y = r
    return x

n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    print((a*b)//re(a,b))
