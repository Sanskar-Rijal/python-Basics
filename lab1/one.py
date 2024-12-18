def checkevenorodd(num:int)->bool:
    if(num%2)== 0:
        return True
    else:
        return False




num=int(input("Enter a number"))
if checkevenorodd(num=num):
    print(f"{num} is even")
else:
    print(f"{num} it is odd")