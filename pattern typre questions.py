#how to approach

#   1.number of lines(rows and columns)=numbber of rows =number of times=number of outer lines
#   2.you can start  first leftside of the pattern amd spaces






n=int(input("enter the number of rows:"))
for i in range (n):
    for j in range (n):
        print("*",end=' ')
    print ()    

n=5
for i in range (n):
    for j in range (i+1):
        print("*",end='  ')
    print()    

n=5
for i in range (n):
    for j in range (i,n):
        print("*",end='  ')
    print()    



#right sided traingle(decreasing space and increasing a star)

n=6
for i in range (n):
    for j in range (i,n):
        print(" ",end='')
    for k in range (i+1):
            print("*",end='')
    print()    

#

n=5
for i in range (n):
    for j in range (i+1):
        print (' ',end='')
    for k in range (i,n):
        print('*',end='')
    print()    

#pyramid


n=5
for i in range (n):
    for j in range (i,n):
        print(' ',end='')
    for k in range (i):
        print('*',end='')
    for g in range(i+1):
        print("*",end='')
    print()    

# reverse pyramid


n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for k in range (i,n):
        print('*',end='')
    for g in range(i,n):
        print('*',end='')
    print()   
    

#diamond pattern

    














        
