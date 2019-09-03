def solution(numbers):
    print(numbers)
    answer = ''
    temp = sorted(numbers)
    print(temp)
    for j in temp:
        for i in range(0,10):
            if j == i:
                answer += j
    return answer
# 처음에는 나눗셈 몫(10)을 사용해서 구현해보려고 했으나 numbers가 0 or 1000까지의 양의 정수이므로 패스
# 나눗셈 몫(10,100)을 사용해서 구현해보려고 했으나 34 35의 경우 비교할 방법이 없어서 패스
