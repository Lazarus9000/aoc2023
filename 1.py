f = open("1.txt", "r")
input = f.read().splitlines() #read lines to list
readcount = 0 #count lines read
cal = [] #Array to hold sums
tempcal = 0 #temp var to calculate elf total cal

while readcount < len(input) :
    
    if input[readcount] != "" :
        first = True
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

#print(len(cal))

for element in cal:
    sum = sum + int(element)
print("day 1 - 1")
print(sum)

readcount = 0 #count lines read
cal = [] #Array to hold sums

while readcount < len(input) :
    
    if input[readcount] != "" :
        first = True
        firstnum = 0
        lastnum = 0
        
        #Issue is that the end of "one" can overlap "eight", two and one, three and eight, etc. code below doesnt handle this
        input[readcount] = input[readcount].replace('oneight', '18')
        input[readcount] = input[readcount].replace('twone', '21')
        input[readcount] = input[readcount].replace('threeight', '38')
        input[readcount] = input[readcount].replace('fiveight', '58')
        input[readcount] = input[readcount].replace('sevenine', '79')
        input[readcount] = input[readcount].replace('eighthree', '83')
        input[readcount] = input[readcount].replace('eightwo', '82')
        input[readcount] = input[readcount].replace('nineight', '98')
        
        input[readcount] = input[readcount].replace('one', '1')
        input[readcount] = input[readcount].replace('two', '2')
        input[readcount] = input[readcount].replace('three', '3')
        input[readcount] = input[readcount].replace('four', '4')
        input[readcount] = input[readcount].replace('five', '5')
        input[readcount] = input[readcount].replace('six', '6')
        input[readcount] = input[readcount].replace('seven', '7')
        input[readcount] = input[readcount].replace('eight', '8')
        input[readcount] = input[readcount].replace('nine', '9')
        
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

print(input)
print(cal)
sum = 0

print(len(cal))

for element in cal:
    sum = sum + int(element)

print("day 1 - 2")
print(sum)