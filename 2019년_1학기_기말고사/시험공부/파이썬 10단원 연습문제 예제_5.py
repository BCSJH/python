class Person(object):
    def __init__(self,name,age,position):
        self.Name = name
        self.Age = age
        self.Position = position

    def show_info(self):
        print("이름 : {}".format(self.Name))
        print("나이 : {}".format(self.Age))
        print("직위 : {}".format(self.Position))
        print("저는 한국성서대학교 연구소 {0} {1} 입니다. 나이는 {2} 입니다.".format(self.Position,self.Name,self.Age))
class Researcher(Person):
    def __init__(self,name,age,position,degree):
        Person.__init__(self,name,age,position)
        self.Degree = degree
    def show_info(self):
        Person.show_info(self)
        print("저는 {} 입니다.".format(self.Degree))

if __name__ == '__main__':
    researcher_john = Researcher("John", "22", "연구원", "학사")
    researcher_Tedd = Researcher("Tedd", "40", "소장", "박사")
    researcher_john.show_info()
    print("="*50)
    researcher_Tedd.show_info()
