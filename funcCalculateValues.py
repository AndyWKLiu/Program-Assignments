def calculateValues(num, value, word):
    if(int(value) < num):
        return True
    elif(value != word and len(word) < 10):
        return True 
    else: 
        return False 
print(calculateValues(4, "7", "clocking"))

#a) 3 
#b) Boolean
#c) line 4 
#d) value != word and len(word) < 10