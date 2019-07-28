#2839
f = int(input())
counts = f
for i in range(int(f/5)+1):
    for ii in range(int(f/3)+1):
        if i*5 + ii*3 == f:
            if counts>i+ii:
                counts = i+ii
if counts ==f:
    print(-1)
else:
    print(counts)
#5x + 3y = f