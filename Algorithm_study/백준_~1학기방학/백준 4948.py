#4948
while True:
    num_count = 0
    n = int(input())
    if n != 0:
        for i in range(n+1,n*2+1):
            check = True
            if i != 1:
                for j in range(2,i):
                    if i % j == 0:
                        check = False
            else:
                check = False
            if check == True:
                num_count += 1
        print(num_count)
    else:
        exit()