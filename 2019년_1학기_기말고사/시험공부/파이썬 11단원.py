#예상 문제
class fuck(object):
    def __init__(self,name,position,back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change(self,new_number):
        print("선수의 등번호를 변경한다. Form %d to %d" %(self.back_number, new_number))
        back_number = new_number
    def __str__(self):
        return "my number is %s, I play in %s in center" %(self.name,self.position)

names = ["Messi", "Ramos","Ronaldo","Park","Buffon"]
positions = ["MF","HT","DF","GK","CF"]
numbers = [10,4,3,2,5]

players = [[name, position, number] for name,position,number in zip(names,positions,numbers)]
print(players)
print(players[0])
players_object = [fuck(name,position,number) for name,position,number in zip(names,positions,numbers)]
jin = fuck(names[0],positions[0],numbers[0])
print("현재 등번호 : ",jin.back_number)
jin.change(5)
print("현재 등번호 : ",jin.back_number)
print(players_object[0])