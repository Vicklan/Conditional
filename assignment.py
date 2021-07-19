def printVowels(sentence):
    
    for x in sentence:
        if (x =='a'or x=='e' or x == 'i' or x == 'o' or x =='u' or x =='A'or x=='E' or x == 'I' or x == 'O' or x =='U'):
            print(x)

sentence = input("Enter your sentence: ")
printVowels(sentence)



