#
INHERITANCE

class dad():
    def phone(self):
        print("dad phone")


class mom():
    def sweet(self):
        print("mom sweet")

class son(dad,mom):
    def laptop(self):
        print(" son laptop")



ram=son()
ram.phone()     
ram.sweet()




# MULTI LEVEL INHERITANCE

class grandpa ():
    def phone(self):
        print("grandpa phone")


class dad (grandpa):
    def money(self):
        print("dad money")

class son(dad):
    def laptop(self):
        print("son laptop")


siva=son()
siva.phone()

#HIERARCHY INHERTANCE


class dad ():
    def money(self):
        print(" dad money ")
class land():
    def important(self):
        print("important land")
        
class son1(dad,land):
    pass
    
class son2(dad):
    pass

class son3(dad):
    pass
    

s2=son2
s2.money()












    
