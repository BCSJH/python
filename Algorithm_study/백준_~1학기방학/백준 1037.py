#1037

n = int(input())
mins = 0
maxs = 0
ns = list(map(int,input().split()))
for i in range(len(ns)):
    if i: # i가 0일 때
        if ns[i] > maxs:
            maxs = ns[i]
        if ns[i] < mins:
            mins = ns[i]
    else:
        maxs = ns[i]
        mins = ns[i]
print(maxs * mins)