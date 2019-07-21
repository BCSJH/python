#15596

def solve(a):
    ans = 0
    for n in range(1,len(a)):
        ans += int(a[n])
    return ans
