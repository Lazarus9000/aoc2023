f = open("9-test.txt", "r")
input = f.read() #read lines to list
#input = "Time:      7  15   30\nDistance:  9  40  200"
inputs = input.split("\n")
#inputs = ["5 11 17 23 29 35 41 47 53 59 65 71 77 83 89 95 101 107 113 119 125"]


results = []
for i in range(len(inputs)):
    upper = inputs[i].split()
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
        
        tempsum = 0
        #Check for empty line - and stop if found
        for k in range(0,len(upper)):
            if nodes[j][k] != 'x':
                tempsum += nodes[j][k]
        
        if tempsum == 0:
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
    for node in nodes:
        print(node)
    
    results.append(nodes[0][len(upper)])
    
#print(nodes)
sum = 0      
for result in results:
    #print(result)
    sum += result
    
print("day 9 - 1")
print(sum)
print()
