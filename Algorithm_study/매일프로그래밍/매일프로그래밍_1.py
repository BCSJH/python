#매일프로그래밍
#0,1,2로만 이루어진 정수 배열을 정렬하시오.
#input [0,1,2,2,1,0]
#output [0,0,1,1,2,2]
#input [1,0,0,0,2]
#output [0,0,0,1,2]

n = list(map(int,input().split()))
print(sorted(n))
