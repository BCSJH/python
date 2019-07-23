#4948
def _4948():
    b = [False,False] + [True]*250000
    for i in range(2,250000):
        if b[i]:
            for j in range(2*i,250000,i):
                b[j] = False

    while True:
        num_count = 0
        n = int(input())
        if n == 0:
            exit()
        for n in range(n+1,n*2+1):
            if b[n]:
                num_count += 1
        print(num_count)

_4948()