from collections import Counter

def freqCounter(sent):
    count= Counter(sent)
    return count

sent=str(input("enter a sentence "))
count= freqCounter(sent)
for char , i in  count.items():
    print(f"{char}:{i}")