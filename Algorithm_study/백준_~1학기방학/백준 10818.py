#10818번
n = int(input())
i = input().split()
min = int(i[0])
max = int(i[0])
for ii in range(n):
    if min>int(i[ii]):
        min = int(i[ii])
    if max<int(i[ii]):
        max = int(i[ii])
print(min, max)
