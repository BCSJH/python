# 선수 등번호 변경

class player(object):
    def __init__(self,name,position,back_number):
        self.name = name
        self.position= position
        self.back_number = back_number
    def change_back_number(self,new_number):
        self.back_number = new_number

jin = player("jinho","MF",10)
print("현재 등번호 : ", jin.back_number)
jin.change_back_number(15)
print("현재 등번호 : ", jin.back_number)