def getSentencelen(sentence:str):
    return (len(sentence.split()))

sent=str(input("enter a sentence "))
count=getSentencelen(sent)
print(f"the number of word is ${count}")