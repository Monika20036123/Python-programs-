class a():
    def __init__(self):
        print("a")
        
    def display():
        print("you r in class a" )


class b(a):
    def __init__(self):
        super().__init__()
        print("b")
    def display():
        print("you r in class b" )


class c(b):
    def __init__(self):
        super().__init__()
        print("c")
    def display():
        print("you are in class c")
        

obj1=c()


