#4153
while (True):
    n = list(map(int, input().split()))
    if (sum(n) == 0):
        break

    h = max(n);
    n.remove(h)
    num = sum(list(map(lambda x: x ** 2, n)))
    if ((h ** 2) == num):
        print('right')
    else:
        print('wrong')