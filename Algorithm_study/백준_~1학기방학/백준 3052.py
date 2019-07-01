#3052번
lists = []
for i in range(10):
    u = input()
    lists.append(int(u)%42)
print(len(list(set(lists))))