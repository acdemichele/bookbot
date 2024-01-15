# print("hello world")
import string



def main():
    path_to_book_file = "books/frankenstein.txt"  
    bookText = getBookFile(path_to_book_file)
    letterCountDict = countLetters(bookText)
    
    print(bookText)
    print(letterCountDict)
    # print(f"The book has {countNumberOfWords(bookText)} words.")
    generateReport(bookText)
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
        
def generateReport(text):
    
    letterDict = countLetters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"The book has {countNumberOfWords(text)} words")
    
    sortedLetterDictByWordCount = sorted(letterDict.items(), key=lambda x:x[1], reverse=True)
    
    convertedDict = dict(sortedLetterDictByWordCount)
    
    for key, value in convertedDict.items():
        
        print(f"The {key} character was found {value} times")

    
    
main()