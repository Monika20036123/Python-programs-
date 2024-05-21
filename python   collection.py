# list

a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
a.extend(b)
print (a)
#list-----> 1.insert,2.pop(remove),3.apppend,4.extend

#tuples

a=(1,2,3,4,5)
b=list(a)
b.pop(4)
print (a)
print(b)


#set

a={1,2,3,4,5,6,1}
a.pop()
print(a)



#1.add,2.pop,4.(remove),3.update

#dictionary

a={"name:monika","age:19","place:arni","a=[1,2,3,4,5,6]"}

del a
print(a)
