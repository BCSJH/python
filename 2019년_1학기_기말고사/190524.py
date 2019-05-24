class SoccerPlayer(object):
    def __init__(self,name, position, back_number):
        # self : 문법적인 규약...인스턴스가 클래스에 접근하기 위해 필
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self,new_number):
        print("선수 등번호를 변경한다 : Form %d to %d" %(self.back_number,new_number))
        self.back_number = new_number
    def __str__(self):
        return "Hello, My name is %s. I play in %s in center." %(self.name, self.position)
class Employee(object):
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'

    def full_name(self):
        return "{} {}".format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay*1.1)

emp_1 = Employee('Sanhee','Lee',50000)
emp_2 = Employee('Minjung','Kim',60000)

print (emp_1.pay)
emp_1.apply_raise()
print (emp_1.pay)


names = ["Messi","Ramos","Ronaldo","Park","Buffon"]
positions = ["MF","DF","CF","WF","GK"]
numbers = [10,4,7,13,1]
players = [[name,position,number] for name, position,number in zip(names,positions,numbers)]
print (players)
print(players[0])
player_objects = [SoccerPlayer(name,position,number) for name, position, number in zip(names,positions,numbers)]
print(player_objects[0])


for _ in range(10):
    print("Hello, World")
    # __init__ : 인스턴스 만들 때 실행되는 함수
    # __str__ : 인스턴스 자체를 출력할 때의 형식을 지정해주는 함수
