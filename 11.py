#f = open("11-test.txt", "r")
f = open("11.txt", "r")
fileinput = f.read() #read lines to list
inputs = fileinput.split("\n")

#print(inputs)

start = (0,0)
check = True
for i in range(len(inputs)):
    if(check):
        empty = all(char == '.' for char in inputs[i])
        if(empty):
            print(i)
            #Insert copy of row
            inputs.insert(i, inputs[i])
            #Used to skip checking the duplicate just made
            check = False
    else:
        check = True
        

check = True


addedrows = 0
for j in range(len(inputs[0])):
    print(j)
    if(check):
        row = []
        for i in range(len(inputs)):
            row.insert(i, inputs[i][j])
        
        #print(row)
        empty = all(char == '.' for char in row)
        if(empty):
            print(j)
            for i in range(len(inputs)):
                inputs[i] = inputs[i][:j] + "." + inputs[i][j:]
            
            addedrows = addedrows + 1
            check = False
    else:
        check = True
        
#this  duplication is ugly
check = True
for j in range(len(inputs[0])-addedrows,len(inputs[0])):
    print(j)
    if(check):
        row = []
        for i in range(len(inputs)):
            row.insert(i, inputs[i][j])
        
        #print(row)
        empty = all(char == '.' for char in row)
        if(empty):
            print(j)
            for i in range(len(inputs)):
                inputs[i] = inputs[i][:j] + "." + inputs[i][j:]
            
            addedrows = addedrows + 1
            check = False
    else:
        check = True

for i in range(len(inputs)):
    print(inputs[i])

class galaxy:
    
    id = 0
    x = 0
    y = 0

class pair:
    id1 = 0
    id2 = 0
    distance = 0

countgalaxy = 0

iditer = 0 
galaxies = []
j = 0
for i in range(len(inputs)):
    for j in range(len(inputs[0])):
        if(inputs[i][j] != "."):
            found = galaxy()
            found.x = j
            found.y = i
            found.id = iditer
            galaxies.append(found)
            iditer = iditer + 1
            
#for galaxy in galaxies:
    #print(galaxy.id)
    #print(galaxy.x)
    #print(galaxy.y)
    #print("-")

pairs = []
for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        found = pair()
        found.id1 = galaxies[i].id
        found.id2 = galaxies[j].id
        #distance
        found.distance = abs(galaxies[i].x-galaxies[j].x) + abs(galaxies[i].y-galaxies[j].y)
        pairs.append(found)
        
print("pairs found: " + str(len(pairs)))

total = 0
for pair in pairs:
    total = total + pair.distance
    
print(total)
#for pair in pairs:
#    print(str(pair.id1+1) + ", " + str(pair.id2+1) + " - dist: " + str(pair.distance))
    

#print(str(galaxies[2].x) + ", " + str(galaxies[2].y))
#print(str(galaxies[5].x) + ", " + str(galaxies[5].y))
#print(abs(galaxies[2].x-galaxies[5].x))
#print(abs(galaxies[2].y-galaxies[5].y))

