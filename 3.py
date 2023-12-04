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
    
    print(numbers)
    
    symbol = False
    
    for number in numbers:
        #print(inputtxt.find(number))
        startno = inputtxt.find(number)
        print(number)
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
                if(char == '*'):
                    print("found #")
                    for x2 in range(x-1,x+1):
                        for y2 in range(y-1,y+1):
                            #error here
                            if(!(startno < x2 > endno and y2 = y)):
                            #if(x2 != x and y2 != y):
                                if(input[y2][x2].isdigit()):
                                    print(number)
                                    print(x2)
                                    print(y2)
                                    gear = seperate_string_number(input[y2][x2-2:x2+2])
                                    print(gear)
                                    sum2 = int(gear[0])*int(number)
                        #print(char + ' found for ' + number)
        
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