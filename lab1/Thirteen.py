def swapstrings(string:str):
    final=string.swapcase()
    return final

sent=str(input("enter a string in lowerand uppercase"))
print(f"initial string is {sent} and final string is {swapstrings(sent)}")
