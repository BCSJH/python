#1316번
counts = 0
i = int(input())
for i in range(i):
    r = input()
    for ii in range(len(r)):
        if r.count(r[ii])>1:
            if ii != len(r)-1:
                if r[ii] == r[ii+1]:
                    continue
                else:
                    if r[ii] == r[ii-1]:
                        continue
                    else:
                        break
        else:
            if ii == (len(r)-1):
                counts += 1
            else:
                continue
print(counts)