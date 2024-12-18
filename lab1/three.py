def calcluator(num1:float,num2:float):
    sum=num1+num2
    if(num1>num2):
        diff=num1-num2
    else:
        diff=num2-num1
    product=num1*num2
    div=num1 / num2
    finaltuple=(f"sum of two number is {sum}",
                f"diff of two number is{diff}",
                f"product of two number is {product}",
                f"division of two number is {div}")
    return finaltuple

firstno = float(input("Enter first number \n"))
secondno=float(input("Enter second number \n"))
answer =calcluator(firstno,secondno)
for n in answer: 
    print(f"{n} \n")