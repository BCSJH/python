#백준 2884
#입력 시간은 24시간 표현을 사용한다.
#24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다.
#시간을 나타낼 때, 불필요한 0은 사용하지 않는다.
time = input().split()
time_1 = int(time[0])
time_2 = int(time[1])
if time_2 < 45:
    if time_1==0:#이걸 안써서 틀림...
        time_1 = 23
    else:
        time_1 = time_1-1
    time_2 = time_2 + 15
else:
    time_2 = time_2 - 45
print(time_1,time_2)