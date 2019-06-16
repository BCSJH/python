class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def about_me(self):
        print("저의 이름은",self.name,"이고요, 나이는 ", str(self.age), " 살입니다.")

#사람에 대한 정의와 일하는 시간과 월급에 대한 변수 추가
class Employee(Person):
    def __init__(self,name,age,gender,salary,hire_date):
        super().__init__(name,age,gender)
        self.salary = salary
        self.hire_date = hire_date

    def do_work(self):
        print("열심히 일을 한다.")
    def about_me(self):
        super().about_me()
        print("제 급여는",self.salary,"원이고, 제 입사일은 ",self.hire_date,"입니다.")

