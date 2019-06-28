#10872번
n = int(input())
sums = 1
for i in range(n):
    sums *= (i+1)
print(sums)
