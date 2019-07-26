#1003
z=[1,0,1]
f=[0,1,1]

def fibonacci(n):#6
    l=len(z)#3
    if l<=n:
        for i in range(l,n+1):
            z.append(z[i-1]+z[i-2])
            f.append(f[i-1]+f[i-2])
    print('%d %d'%(z[n],f[n]))
for _ in range(int(input())):
    fibonacci(int(input()))