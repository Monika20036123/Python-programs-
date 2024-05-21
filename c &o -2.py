class laptop:
    def __init__(self):
       
       self.proc=""
       self.ram=""
    def display(self):
        print ("ram:",self.ram)
        print("proc:",self.proc)

hp=laptop()
dell=laptop()

dell.ram="16gb"
dell.proc="i7"

hp.proc="i5"
hp.ram="8gb"

                                                        
hp.display()

dell.display()
