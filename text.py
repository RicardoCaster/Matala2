#Matala2
#Ricardo

def revword(word):
    try:
        word = (word.lower())
        return word[::-1]
    except:
        return "There is a problem"


def countword():
    try:
        #file = input("enter file: ")
        fhandle = open("text.txt" , "r")
        count = 0
        
        for line in fhandle:
            line = line.rstrip()
            strings = line.split()
            word = strings[0]        
            break
        
        for line in fhandle:
            line = line.rstrip()
            strings = line.split()
            for string in strings:
                real_string = revword(string)            
                if real_string == word:                
                    count+=1   
        return count+1
    except:
        return "Your file has a problem."
        

            
            
            
    