from collections import defaultdict
import operator
def solution(N, stages):
    # 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
    # N = 전체 스테이지의 수 (1 <= N <= 500)
    # states = 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 긴 배열
    # (1 <= len(stages) <= 20000)
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열 return
    # stages에는 1이상 N+1이하의 자연수가 담겨져 있다.
    # N+1은 마지막 스테이지까지 클리어한 사용자를 나타낸다.

    # 전체 스테이지 수가 5개
    # stages = [2,1,2,6,2,4,3,3] 총 8명

    answer = []
    answer_count = []
    answer_count_percent = dict()
    answer_dic = dict()
    #answer_count = Counter(N)
    #print(answer_count)
    #for i in range(N+1):
    #    answer.append(float(int(answer_count[i])/N))
    for i in range(0,N+1):
        sums_u = 0
        sums_d = 0
        print("i : ",i)
        answer_count.append(stages.count(i+1))
        print(answer_count)
        for ii in range(0, i+1):
            print(ii+1, "번째 ii : ", ii)
            if ii == 0:
                continue
            else:
                sums_d += answer_count[ii-1]
        sums_u = answer_count[i]
        print("sums_u ; ", sums_u)
        print("stages ; ", len(stages))
        print("sums_d ; ", sums_d)
        answer_count_percent[i+1] = ((sums_u) / (len(stages) - sums_d))
        #answer_count_percent.append((sums_u)/(len(stages)-sums_d))
    answer_dic = sorted(answer_count_percent.items(), key=lambda x: x[1], reverse=True)
    #answer_dic = sorted(answer_count_percent.items(), key=operator.itemgetter(1))
    print(answer_count_percent)
    print(answer_dic)
    print(answer_count)


    return answer

print("정답" + solution(5,[2,1,2,6,2,4,3,3]))
print("정답" + solution(4,[4,4,4,4,4]))