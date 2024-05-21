list=[1,2,3,4,5,6]
search=int(input())
for  i in range(0,len(list)):
     if search==list[i]:
         print(str(search)+"found at position"+str(i))
