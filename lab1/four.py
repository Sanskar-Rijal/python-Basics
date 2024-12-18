def primeorcomposite(num1:int,num2:int)->bool:
    if(num1%num2)==0:
        return True #composite
    else:
        return False #prime


for i in range (2,101): # 7
    flag:int=0
    for j in range(2,i//2+1):  #3
        if(primeorcomposite(i,j)): 
            flag=1 #7/1 7/2 7/3
            break
    if(flag==0):
     print(f"{i} is prime number")
