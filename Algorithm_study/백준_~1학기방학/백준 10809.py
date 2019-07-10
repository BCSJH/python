#10809번
from string import ascii_lowercase
a = list(ascii_lowercase)
number = 0
n = input()
for i in a:
    if n.count(i)>=0:
        print(n.find(i), end=' ')
    else:
        print("-1", end=' ')
