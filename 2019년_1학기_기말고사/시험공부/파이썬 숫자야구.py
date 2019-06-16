
#\ class를 이용한 숫자야구

import random
class playball(object):
    def __init__(self, computer, user):
        self.computer = computer
        self.user = user
        self.number = 0
        self.strike = 0
        self.ball = 0
        self.out = 0

    def check(self, computer, user):
        for number in computer:
            if user.find(number) == computer.find(number):
                self.strike += 1
            elif user.find(number) >= 0:
                self.ball += 1

        print("strike : ", self.strike, "ball : ", self.ball)
        self.number += 1
        if self.strike == 3:
            print("정답입니다.", self.number, '만에 맞췄습니다.')
            return 0
        self.strike = 0
        self.ball = 0
computer_number = ""
user = ""
cc=0
baseball = playball(computer_number,user)
while cc < 3:
    computer = str(random.randint(1, 9))
    if computer_number.find(computer) >= 0:
        continue
    else:
        computer_number += computer
        cc += 1

print(computer_number)
while 1:
    user = input("입력 : ")
    if(baseball.check(user,computer_number)==0):
        break


