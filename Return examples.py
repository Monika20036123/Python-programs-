s_username="EMC"
s_pssword="123"

u_name =input("enter a value for u_name:")
password=input("enter a value for password:")

def validate():
    if(s_username==u_name and s_pssword==password):
        return True
    else:
       return False

a=validate()
print(a)        



def add(n1,n2):
    return n1+n2
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
added=a+b
output=added*c
print(output)
