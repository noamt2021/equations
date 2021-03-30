#fhand = open("test.txt")
#text= fhand.read()
#print(text)

def revword(word):
    newword = word[::-1].lower()
    return newword
def countword():
    counter=1
    fhand = open("text.txt")
    text= fhand.read()
    word = text.split()[0]
    
    for h in text.split():
        if revword(h) == word:
           counter+= 1
    return counter        
      
        



           






 

 

