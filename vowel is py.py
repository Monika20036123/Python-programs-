s=input("enter a string:")
c=0
for i in s:
    if i in "aeiouAEIOU":
        c+=1
print("the number of vowels ",s,"is",c)    
