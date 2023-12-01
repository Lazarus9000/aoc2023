f = open("1.txt", "r")
input = f.read().splitlines() #read lines to list
readcount = 0 #count lines read
cal = [] #Array to hold sums
tempcal = 0 #temp var to calculate elf total cal

while readcount < len(input) :
    
    if input[readcount] != "" :
        first = True
        last = False
        firstnum = 0
        lastnum = 0
        for element in input[readcount]:
            if element.isnumeric():
                if first:
                    first = False
                    firstnum = element
                else:
                    lastnum = element
        
        if lastnum == 0:
            lastnum = firstnum
        
        cal.append(firstnum + lastnum)
        
    readcount += 1 #increment line to read
    
sum = 0

print(len(cal))

for element in cal:
    sum = sum + int(element)

print(sum)
