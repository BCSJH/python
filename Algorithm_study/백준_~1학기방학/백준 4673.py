# 4673번
n = set(range(1,10001))
nn = set()
for i in range(1,10001):
    for ii in str(i):
        i += int(ii)
    nn.add(i)
nnn = n - nn
for i in sorted(nnn):
    print(i)