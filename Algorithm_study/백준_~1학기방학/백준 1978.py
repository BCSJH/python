#1978번
count = 0
n = int(input())
lists = map(int,input().split())
for i in lists:
    check = True
    if i != 1:
         for f in range(2,i):
             if i % f == 0:
                 check = False
    else:
        check = False
    if check == True:
        count+=1
print(count)
