f = open("3.txt", "r")
input = f.read().splitlines() #read lines to list
readcount = 0 #count lines read
cal = [] #Array to hold sums
tempcal = 0 #temp var to calculate elf total cal
input_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
sum = 0

#https://stackoverflow.com/questions/430079/how-to-split-strings-into-text-and-number
def seperate_string_number(string):
    previous_character = string[0]
    groups = []
    newword = string[0]
    for x, i in enumerate(string[1:]):
        if i.isalpha() and previous_character.isalpha():
            newword += i
        elif i.isnumeric() and previous_character.isnumeric():
            newword += i
        else:
            groups.append(newword)
            newword = i

        previous_character = i

        if x == len(string) - 2:
            groups.append(newword)
            newword = ''
    return groups

while readcount < len(input) :
    inputtxt = input[readcount]
    numbers = []
    #print(inputtxt)
    
    groups = seperate_string_number(inputtxt)
    for group in groups:
        if group.isdigit():
            numbers.append(group)
    
    #for s in inputtxt.split('.'):
    #    if s.isdigit():
    #        numbers.append(s)
    
    #print(numbers)
    
    symbol = False
    
    for number in numbers:
        #print(inputtxt.find(number))
        startno = inputtxt.find(number)
        #print(number)
        endno = startno+len(number)
        
        xmin = max(startno -1, 0)
        xmax = min(endno, len(inputtxt))
        
        ymin = max(readcount - 1,0)
        ymax = min(readcount + 1, len(input))
        
        
        #print(xmin)
        #print(xmax)
        #print(ymin)
        #print(ymax)
        
        for x in range(xmin, min(xmax+1,len(inputtxt))):
            for y in range(ymin, min(ymax+1,len(input))):
                char = input[y][x]
                #print(char)
                if(not char.isdigit()):
                    if(char != '.'):
                        symbol = True
                        #print(char + ' found for ' + number)
        
        if(symbol):
            sum+=int(number)
        #else:
            #print(number + ' is not part of the sum')
        
        #Had to clean up to find multiple instances of a number - find only returns the first
        for pos in range(startno, endno):
            temp = list(inputtxt)
            temp[pos] = '.'
            inputtxt = "".join(temp)
            #print(inputtxt)
            
        symbol = False
    #increment line to read        
    readcount += 1         
            
print("day 3 - 1")
print(sum)




readcount = 0
sum2 = 0
results = []

while readcount < len(input) :
    inputtxt = input[readcount]
    numbers = []
    #print(inputtxt)
    
    groups = seperate_string_number(inputtxt)
    for group in groups:
        if group.isdigit():
            numbers.append(group)
    
    #for s in inputtxt.split('.'):
    #    if s.isdigit():
    #        numbers.append(s)
    
    #print(numbers)
    
    symbol = False
    
    for number in numbers:
        #print(inputtxt.find(number))
        startno = inputtxt.find(number)
        #print(number)
        endno = startno+len(number)
        
        #print(startno)
        #print(endno)
        
        xmin = max(startno -1, 0)
        #xmin = max(startno, 0)
        xmax = min(endno, len(inputtxt))
        
        ymin = max(readcount - 1,0)
        #Don't search up - might find a gear that was already found in earlier scan
        #ymin = max(readcount,0)
        
        ymax = min(readcount + 1, len(input))
        
        
        #print(xmin)
        #print(xmax)
        #print(ymin)
        #print(ymax)
        
        found = False
        for x in range(xmin, min(xmax+1,len(inputtxt))):
            for y in range(ymin, min(ymax+1,len(input))):
                #Special case - found numbers on the same line twice
                if(not(x==xmin and y==readcount) and not(x<endno and y==ymin)):
                    char = input[y][x]
                    #print(char)
                    if(char == '*'):
                        #print("found *")
                        
                        #search area around *
                        #Only search to the right
                        for x2 in range(x-1,x+2):
                            for y2 in range(y-1,y+2):
                                #Special case - don't search left up diagonal
                                #if(not(x2==x-1 and y2==y-1) and not(x2==x-1 and y2 == y)):
                                if(True):
                                    #print(str(x2) + ", " + str(y2))
                                    
                                    #don't find original number
                                    sameno = (startno <= x2 <= endno and y2 == readcount)
                                    
                                    #Dont look left
                                    left = (y2==y and x2==x-1)
                                    
                                    #dont look top left and middle
                                    top = (x2<x and y2==y-1)
                                    
                                    
                                    
                                    if(not(sameno) and not(left) and not(top) and not(x2==x+1 and y2 == y-1 and x==xmax and y==ymin)):
                                    
                                    #if(x2 != x and y2 != y):
                                        char2 = input[y2][x2]
                                        number2 = char2
                                        #print(char2 + "found at " + str(x2) + ", " + str(y2))
                                        if(char2.isnumeric()):
                                            
                                            #print(x2)
                                            #print(y2)
                                            char3 = ""
                                            x3 = x2
                                            while(char3 != "." and char3 != "*"):
                                                char3 = input[y2][x3-1]
                                                if(char3.isnumeric()):
                                                    number2 = char3 + number2
                                                x3 = x3-1
                                                
                                            char3 = ""
                                            x3 = x2
                                            while(char3 != "." and char3 != "*"):
                                                char3 = input[y2][x3+1]
                                                if(char3.isnumeric()):
                                                    number2 = number2 + char3
                                                x3 = x3+1
                                            
                                            result = int(number2)*int(number)
                                            
                                            #print("number 1: " + number + ", number 2: " + number2 + " - " + str(result))
                                            
                                            trueresult = True
                                            
                                            #Check for dublet results - assumes that all gears are individual
                                            for r in results:
                                                #print(r)
                                                if r == result:
                                                    #print("Fake results!")
                                                    trueresult = False
                                                #else:
                                                    #print("true result")
                                            
                                            if(trueresult):
                                                
                                                sum2 += result
                                                results.append(result)
                                                
                                               # print("number 1: " + number + ", number 2: " + number2 + " - " + str(result) + " " + str(trueresult))
                                            #print(results)
                                            found = True
                                            break
                                                
                                    #Avoid duplicate finds if two chars of a number is in the search area
                                    if(found):
                                        break
                            #Avoid duplicate finds if two chars of a number is in the search area
                            if(found):
                                break
                    
                    if(found):
                        break                #print(char + ' found for ' + number)
            if(found):
                break
          
        #if(symbol):
        #    sum+=int(number)
        #else:
            #print(number + ' is not part of the sum')
        
        #Had to clean up to find multiple instances of a number - find only returns the first
        for pos in range(startno, endno):
            temp = list(inputtxt)
            temp[pos] = '.'
            inputtxt = "".join(temp)
            #print(inputtxt)
            
        #symbol = False
    #increment line to read        
    readcount += 1   


print("day 3 - 2")
print (sum2)


readcount = 0
sum2 = 0
results = []

while readcount < len(input) :
    inputtxt = input[readcount]
    
    for charpos in range(len(inputtxt)):
        char = inputtxt[charpos]
        if char == "*":
            #print("* found on " + str(readcount) + " - " + str(charpos))
            numbers = []
            for y in range(readcount-1, readcount+2):
                for x in range(charpos-1,charpos+2):
                    #print(input[y][x])
                    if(input[y][x].isnumeric()):
                        
                        tempnumber = input[y][x]
                        
                        char2 = ""
                        x2 = x
                        while(char2 != "." and char2 != "*"):
                            char2 = input[y][x2+1]
                            if(char2.isnumeric()):
                                tempnumber = tempnumber + char2
                                x2 = x2+1
                        
                        char2 = ""
                        x2 = x
                        
                        while(char2 != "." and char2 != "*"):
                            char2 = input[y][x2-1]
                            if(char2.isnumeric()):
                                tempnumber = char2 + tempnumber
                            x2 = x2-1
                        
                        #print("temp = " + tempnumber)
                        
                        foundnumber = False
                        for number in numbers:
                            if number == tempnumber:
                                foundnumber = True
                        
                        if not(foundnumber):
                            numbers.append(tempnumber)
            #print(str(numbers) + " - " + str(len(numbers)))
            if len(numbers) == 2:
                sum2 += int(numbers[0]) * int(numbers[1])

    
    readcount += 1 
    
print("day 3 - 2")
print (sum2)
