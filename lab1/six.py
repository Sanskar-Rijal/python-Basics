def getFact(fact:int, i:int):
    fact=fact*i 
    return fact

fact=1
num=int(input("Enter a number"))
for i in range(1,num+1):
    fact=getFact(fact,i)
print(f"the factorial of number is {fact}")