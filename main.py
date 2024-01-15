# print("hello world")
import string



def main():
    path_to_book_file = "books/frankenstein.txt"  
    bookText = getBookFile(path_to_book_file)
    letterCountDict = countLetters(bookText)
    
    print(bookText)
    print(letterCountDict)
    print(f"The book has {countNumberOfWords(bookText)} words.")
    
def getBookFile(path):

    with open(path) as f:
        
        return f.read()

def countNumberOfWords(text):
    
    listOfWords = text.split()
    
    return len(listOfWords)
        
def countLetters(text):
    letterCountDictionary = {}
    listOfLowerCaseLetters = list(string.ascii_lowercase)
    
    listOfWords = text.split()
    
    for letter in listOfLowerCaseLetters:
        numOfTotalAppearances = 0
        for word in listOfWords:
            numOfAppearancesInWord = 0
            lowerCaseWord = word.lower()
            numOfTotalAppearances += lowerCaseWord.count(letter)
        letterCountDictionary[letter] = numOfTotalAppearances    
    return letterCountDictionary    
        
    
    
main()