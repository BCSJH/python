#백준 1330
#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
#A가 B보다 큰 경우에는 '>'를 출력한다.
#A가 B보다 작은 경우에는 '<'를 출력한다.
#A와 B가 같은 경우에는 '=='를 출력한다.
number = input().split()
if int(number[0])>int(number[1]):
    print(">")
elif int(number[0])<int(number[1]):
    print("<")
else:
    print("==")
