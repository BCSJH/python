#백준 2562
ranges = []
for i in range(9):
    ranges.append(int(input()))
print(max(ranges))
print(ranges.index(max(ranges))+1)
#_+1을 해줘야지 멍청아ㅠㅠ 이거때매 틀렸잖아ㅠㅠ