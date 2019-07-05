#2751번
n = int(input())
a=[]
for i in range(n):
    a[i]= int(input())
a.sort()
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        a.remove(i+1)
for i in range(len(a)):
    print(a[i])
