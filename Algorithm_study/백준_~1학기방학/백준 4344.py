#4344번
n =int(input())
for i in range(n):
    sums = 0
    count = 0
    u = input().split()
    for ii in range(len(u)):
        if ii == 0:
            continue
        else:
            sums += int(u[ii])
    sums = sums / int(u[0])
    for ii in range(len(u)):
        if ii == 0:
            continue
        else:
            if sums<int(u[ii]):
                count+=1
    count = (count / int(u[0]))*100
    print('{:.3f}%'.format(count))