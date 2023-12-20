f = open("9.txt", "r")
fileinput = f.read() #read lines to list
#input = "Time:      7  15   30\nDistance:  9  40  200"
inputs = fileinput.split("\n")
#inputs = ["5 11 17 23 29 35 41 47 53 59 65 71 77 83 89 95 101 107 113 119 125"]


results = []
for i in range(len(inputs)):
    upper = inputs[i].split()
    nodetemplate = ['x'] * (len(upper)+1)
    #nodes = [nodetemplate, nodetemplate]
    
    nodes = [['x'] * (len(upper)+1) for x in range(len(upper))]
    #nodes = node*len(upper)
    #print(nodes)
    #First line
    for j in range(len(upper)):
        nodes[0][j] = int(upper[j])
    
    
    low = 0
    empty = False
    #Loop through lines
    for j in range(len(upper)):
        #nodes.append(nodetemplate)
        tempsum = 0
        linecount = 0
        tempcount = 0
        #Check for empty line - and stop if found
        for k in range(0,len(upper)):
            if nodes[j][k] != 'x':
                tempsum += nodes[j][k]
                linecount += 1
            
            #Sum failed for this input, due to the 5th line summing to zero without being all zeroes
            #15 25 54 108 189 298 441 637 927 1383 2116 3282 5085 7776 11647 17019 24223 33573 45330 59656 76557
            
            if nodes[j][k] == 0:
                tempcount += 1
        
        print("tempsum: " + str(tempsum))
        print("tempcount: " + str(tempcount))
        
        if tempcount == linecount:
            #print("empty line")
            empty = True
            break
        
        
        
        #Calculate values of current line
        for k in range(len(upper)):
            if nodes[j][k+1] != 'x':
                low = j+1
                nodes[j+1][k] = nodes[j][k+1] - nodes[j][k]
                
    
    #debugging    
    if not(empty):
        print("no end wtf!")
    #print(nodes)
    #print(low)
    
    #Fill in values to the right
    #Loop through from the lowest level
    for j in range(low,-1,-1):
        found = False
        #print(j)
        #Loop through values in level
        for k in range(len(upper)+1):
            #print(nodes[j][k])
            #Find the rightmost value
            if nodes[j][k] == 'x' and not(found):
                #Found ensures only the rightmost value is used
                found = True
                #For the lowest level, insert extra zero
                if j == low:
                    nodes[j][k] = 0
                else:
                
                    #print(str(j) + ", " + str(k))
                    #print(nodes[j][k-1])
                    #print(nodes[j+1][k-1])
                    nodes[j][k] = nodes[j][k-1] + nodes[j+1][k-1]
    #for node in nodes:
        #print(node)
    
    results.append(nodes[0][len(upper)])
    #input("next")
#print(nodes)
sum = 0      

print("input len: " + str(len(inputs)))
print("results len: " + str(len(results)))

for result in results:
    #print(result)
    sum += result
    
print("day 9 - 1")
print(sum)
print()

#1708206327 - your answer is too high