#1712
a,b,c = list(map(int,input().split()))
i = 0
if c <= b:
    i = -1
else:
    i = a//(c-b)+1
print(i)