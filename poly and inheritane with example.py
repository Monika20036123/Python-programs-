#1

class shape():
    def area (self):
        return 0


class rectangle(shape):
    def area(self):
        l=10
        b=8
        print("area of retangle:",l*b)

        




r1=rectangle()
r1.area()

#2


class person():
    def __init__(self,name):
        self.name=name


class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade


    def display(self):
        print(self.name,self.grade)


s1=student("monika","a")
s1.display()



#3


class vehicle():
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
        print("car started")



v1=car()
v1.start()



#4

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


class manager(employee):
    def __init__(self,department):
        super().__init__("monika","50000")
        self.department=department



    def display(self):
       print(self.name,self.salary,self.department)


m1=manager("ece")
m1.display()


























        
