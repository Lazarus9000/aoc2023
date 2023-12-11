f = open("8.txt", "r")
input = f.read() #read lines to list
#input = "Time:      7  15   30\nDistance:  9  40  200"
inputs = input.split("\n")

from math import lcm

nodes = []
count = 0
instruction = []
for i in range(len(inputs)):
    if i == 0:
        instruction = inputs[i]
        
    if i > 1:
        node = inputs[i].split()
        #print(node)
        nodes.append([node[0], node[2][1:4], node[3][:3]])
    

#print(instruction)
#print()
#print(nodes)
coloumn = [i[0] for i in nodes]
found = False
currentpos = coloumn.index('AAA')
print(currentpos)
currentinstruction = 0
while not(found):
    if instruction[currentinstruction] == "L":
        #print("go left")
        nextpos = coloumn.index(nodes[currentpos][1])
        currentpos = nextpos
    else:
        #print("go right")
        nextpos = coloumn.index(nodes[currentpos][2])
        currentpos = nextpos
    
    count += 1
    
    currentinstruction += 1
    if currentinstruction >= len(instruction):
        currentinstruction = 0
        
    if (nodes[currentpos][0] == 'ZZZ'):
        found = True

print("day 8 - 1")
print(count)
print()

starts = []
for node in nodes:
    if node[0][2] == "A":
        starts.append(coloumn.index(node[0]))

endcounts = []
for start in starts:
    print(nodes[start])
    
    count = 0
    found = False
    currentpos = start
    #print(currentpos)
    currentinstruction = 0
    while not(found):
        if instruction[currentinstruction] == "L":
            #print("go left")
            nextpos = coloumn.index(nodes[currentpos][1])
            currentpos = nextpos
        else:
            #print("go right")
            nextpos = coloumn.index(nodes[currentpos][2])
            currentpos = nextpos
        
        count += 1
        
        currentinstruction += 1
        if currentinstruction >= len(instruction):
            currentinstruction = 0
            
        if (nodes[currentpos][0][2] == 'Z'):
            print(count)
            endcounts.append(count)
            found = True
            
lcm = lcm(endcounts[0], endcounts[1], endcounts[2], endcounts[3], endcounts[4], endcounts[5])

print("day 8 - 2")
print(lcm)
            