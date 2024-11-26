wordcount = dict()
wordlist = input("Enter the string : ").upper().split()
uniqueword = set(wordlist)
for word in uniqueword:
    wordcount[word] = wordlist.count(word)


print(wordcount)