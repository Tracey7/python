class phone:
    def __init__(self,name,yearofmake,color,storage):
        self.name='iPhone'
        self.yearofmake=1999
        self.color='gold'
        self.storage='256gb'


class school:
    def __init__(self,name,age,year):
        self.name=name
        self.age=age
        self.year=year

student1=school('Tracey', '20', '3rd')
student2=school('Elvis','19','2nd')
student3=school('Joseph','20','forth')
print(student1.name)