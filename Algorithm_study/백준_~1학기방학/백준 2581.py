#2581번
sums = 0
mins = 0
first = 1
n = int(input())
nn = int(input())
for i in range(n,nn+1):
    check = True
    if i != 1:
         for f in range(2,i):
             if i % f == 0:
                 check = False
    else:
        check = False
    if check == True:
        if first == 1:
            mins = i
            first = 2
        sums+=i
if sums == 0:
    print(-1)
else:
    print(sums)
    print(mins)
