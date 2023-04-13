# بسم الله الرحمن الرحيم
# صل علي النبي 

# Importing the main libraries
from nltk import sent_tokenize,word_tokenize,PorterStemmer,SnowballStemmer

# A function to tokenize as words
def wordTokenization(word):
    return word_tokenize(word)

# A function to tokenize as sentences
def sentencesTokenization(sentence):
    return sent_tokenize(sentence)

# A function to print the original texts
def printOriginal(text):
    return text

# A function to apply stemming function
def stemWords(sentence):
    # Taking an object from stemming classes
    ps = PorterStemmer()
    sb = SnowballStemmer("english")

    words = word_tokenize(sentence)
    print("\n1- Porter Stemmer\n2- snowball stemmer \n")
    choice = int(input("Enter your choice : "))
    if choice == 1 : 
        stemmedWords = [ps.stem(word) for word in words]
        return stemmedWords
    elif choice == 2 :
        stemmedWords = [sb.stem(word) for word in words]
        return stemmedWords


# The main function of the program
def mainFunction():

    # An infinity loop to keep the program running after results
    while True:

        print("\n1- Print Tokenized words.\n2- print Tokenized sentences.\n3- print the original text.\n4- Stemming.\n5- Exit\n")
        # The choices of the tokenization and calling functions depending on user's choice
        choice = int(input("Enter your choice : "))
        if choice == 1:
            sentence = input("\nEnter the sentence that you want to tokenize it as words : ")
            print(f"\nThe result is : {wordTokenization(sentence)}\n---------------------------------------")
        elif choice == 2:
            sentence = input("\nEnter the sentence that you want to tokenize as sentences : ")
            print(f"\nThe result is : {sentencesTokenization(sentence)}\n---------------------------------------")
        elif choice == 3:
            sentence = input("\nEnter the sentence that you want to print it : ")
            print(f"\nThe result is : {printOriginal(sentence)}\n---------------------------------------")
        elif choice == 4:
            sentence = input("\nEnter the sentence that you want to stem it : ")
            print(f"\nThe result is : {stemWords(sentence)}\n---------------------------------------")
        elif choice == 5:
            break
        else:
            print("\nPlease enter a valid number \n---------------------------------------")
        
# Calling the main function of the program
mainFunction()