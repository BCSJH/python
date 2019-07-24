#1037

n = int(input())
maxs = 1
ns = list(map(int,input().split()))
for i in range(len(ns)):
    maxs *= ns[i]
print(maxs)
