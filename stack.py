l=[]
l.append(1)
l.append(2)
l.append(3)
print(l)

arr=[1,2,3]
b=[]
for i in range(len(arr)):
    b.append(arr.pop())
print(b)    



#stck implementation using list


#top--->current element aa pop pannum  and index always starts in zero
def create_stack():
    stack=[]
    return stack

#creating a empty list

def empty_list(stack):
    return len(stack)==0

# adding items
def push(stack,item):
    stack.append(item)
    print("pushed item:", item)

#removing element    

def pop(stack):
     if(check_empty(stack)):
         return "empty stack"
     return stack.pop()


stack=create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
push(stack,str(5))
print("Popped item:"+pop(stack))
print("stack after popping element:"+str(stack))









    














































































































































