#11279
i = []
n = int(input())
for g in range(n):
    u = int(input())
    if u == 0 and len(i)==0:
        print("0")
    elif u==0:
        print(max(i))
        i.remove(max(i))
    else:
        i.append(u)


