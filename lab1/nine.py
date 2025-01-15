def listsum(list):
    return sum(list)

user=list(map(int,input("enter a list").split()))
print(f"the sum of the numbers you entered in a list is {listsum(user)}")
