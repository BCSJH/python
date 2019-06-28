def solve(a):
    ans = 0
    for i in range(a):
        ans += (i+1)
    return ans
a = int(input())
print(solve(a))
