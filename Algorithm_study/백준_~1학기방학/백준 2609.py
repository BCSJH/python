#2609
def gcd(a,b):
    maxs = max(a, b)
    while True:
        if a % maxs == 0 and b % maxs == 0:
            return maxs
        maxs-=1
def lcm(a,b):
    return (a * b) / gcd(a,b)

a,b = list(map(int,input().split()))
print(gcd(a,b))
print(int(lcm(a,b)))

