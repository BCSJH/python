#1157번
a = []
number = 0
n = input().upper()
a = set(n)
max = n.count(n[0])
for i in a:
    if max < n.count(i):
        max = n.count(i)
for i in a:
    if max == n.count(i):
        number+=1
if number>1:
    print("?")
    exit()
for i in a:
    if max == n.count(i):
        print(i)