class animal():
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("dog barks")


class birds(animal):
    def sound(self):
        print("birds sing")
        

b1=birds()
b1.sound()
