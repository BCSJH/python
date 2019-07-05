#1929번
a = []
n = input().split()
for i in range(int(n[0]),int(n[1])):
    check = True
    if i != 1:
         for f in range(2,i):
             if i % f == 0:
                 check = False
    else:
        check = False
    if check == True:
        a.append(i)
for i in range(len(a)):
    print(a[i])