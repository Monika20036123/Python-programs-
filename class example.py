
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

























       
