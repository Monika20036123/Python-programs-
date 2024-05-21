#1

class student:
    def __init__(self):
        self.name="monika"
        self.regno="6004"
    def display(self):
        print("name:",self.name)
        print("reg no:",self.regno)



s1=student()
s2=student()

s1.name="manoj"
s1.regno="123"

s2.name='Siva'
s2.regno="4018"


s2.display()
s1.display()


#2



class fruit:
    def __init__(self,color):
        self.color=color

apple=fruit("red")
print(apple.color)






#3

class customer:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address


    def myfunction(self):
        print("name:",self.name)
        print("age:",self.age)
        print("address:",self.address)


detail=customer("monika","19","arni")
detail.myfunction()



#4


class teacher:
    def __init__ (self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("name:",self.name)
        print("reg no:",self.regno)



t1=teacher("thomas","1")
t2=teacher("john","2")

t1.display()
t2.display()




#5


class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add:",self.num1+self.num2)

    def sub(self):
        print("sub:",self.num1-self.num2)

    def mul(self):
        print("mul:",self.num1*self.num2)

    def div(self):
        print("div:",self.num1/self.num2)

obj1=calculator(10,2)
obj1.add()

obj2=calculator(99,8)
obj2.sub()


obj3=calculator(7,8)
obj3.mul()

obj4=calculator(6,3)
obj4.div()


















































        
        


















