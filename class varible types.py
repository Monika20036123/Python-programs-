#instance variable type(self kulla value aa assign pandrathukkku name instance variable)

class phone:
    
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.chage="c type"
       

    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("charge:",self.charge)



p1=phone("samsung","10000")
p1.display()

p2=phone("vivo","15000")
p2.display()



# class variables type (class kulla value aa assign pandrathukku name class vrialble )

class phone:
    charge="c type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
       

    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("charge:",self.charge)


p1=phone("samsung","10000")
p1.display()

p2=phone("vivo","15000")
p2.display()
