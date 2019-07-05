#2751
lists = []
ins = int(input())
for _ in range(ins):
    a = int(input())
    lists.append(a)
lists.sort(reverse=False)
for i in range(len(lists)):
    print(lists[i])
