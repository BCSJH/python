#2748
sums = [0,1]
n = int(input())
for i in range(n+1):
    if i != 0 and i != 1:
        sums.append(sums[i-1]+sums[i-2])
    else:
        continue
print(sums[n])



