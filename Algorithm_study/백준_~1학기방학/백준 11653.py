#11653
n = int(input())
check = 2
while True:
    for i in range(2, 1000000):
        if n == 1:
            exit()
        if n % i == 0:
            print(i)
            n = n/i
            break
