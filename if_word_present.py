def isWordPresent(sentence, word):
     
    # To break the sentence in words
    s = sentence.split(" ")
 
    for i in s:
 
        # Comparing the current word
        # with the word to be searched
        if (i == word):
            return True
    return False
 
def main():
    s = "Geeks for Geeks"
    word = "Geeks"
    
    if (isWordPresent(s, word)):
        print("Yes")
    else:
        print("No")
        
if __name__ == '__main__':
    main()