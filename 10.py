f = open("10.txt", "r")
fileinput = f.read() #read lines to list
#input = "Time:      7  15   30\nDistance:  9  40  200"
inputs = fileinput.split("\n")
#inputs = ["5 11 17 23 29 35 41 47 53 59 65 71 77 83 89 95 101 107 113 119 125"]

directions = "|-LJ7F."
compass = "NSWE"

def compassheading(heading):
    next = (0,0)
    if heading == 'N':
        next = (-1,0)
    if heading == 'E':
        next = (0,1)
    if heading == 'W':
        next = (0,-1)
    if heading == 'S':
        next = (1,0)
    return next

def direction(input):
        
    if input == 'F':
        return (-1,0)
    
    if input == '7':
        return (0,-1)
        
    if input == '|':
        return (0,-1)

map = [['x'] * (len(inputs)) for x in range(len(inputs))]
start = (0,0)
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        map[i][j] = inputs[i][j]
        if map[i][j] == 'S':
            start = (i,j)

print(start)

steps = 0
#for i in range(start[0]-1, start[0]+2):
    #check inside border
    #if i > -1 and i < len(inputs):
    #    for j in range(start[1]-1, start[1]+2):
    #        if j > -1 and j < len(inputs[0]):
startfound = False
for startheading in compass:
    if not(startfound):
        heading = startheading
        nextstep = compassheading(heading)
        next = (start[0]+nextstep[0], start[1]+nextstep[1])
        #print("start: " + str(next))
        
        steps = 1
        while not(startfound):
            steps += 1
            nextfound = False
            nextpos = map[next[0]][next[1]]
            #print("nextpos: " + nextpos)
            if heading == 'W' and nextpos == 'J':
                heading = 'N'
                nextfound = True
            
            elif heading == 'W' and nextpos == '7':
                heading = 'S'
                nextfound = True
            
            elif heading == 'W' and nextpos == '-':
                heading = 'W'
                nextfound = True
            
            elif heading == 'N' and nextpos == 'F':
                heading = 'E'
                nextfound = True
            
            elif heading == 'N' and nextpos == '7':
                heading = 'W'
                nextfound = True
            
            elif heading == 'N' and nextpos == '|':
                heading = 'N'
                nextfound = True
            
            elif heading == 'S' and nextpos == 'L':
                heading = 'E'
                nextfound = True
            
            elif heading == 'S' and nextpos == 'J':
                heading = 'W'
                nextfound = True
                
            elif heading == 'S' and nextpos == '|':
                heading = 'S'
                nextfound = True
            
            elif heading == 'E' and nextpos == 'J':
                heading = 'N'
                nextfound = True
            
            elif heading == 'E' and nextpos == '7':
                heading = 'S'
                nextfound = True
            
            elif heading == 'E' and nextpos == '-':
                heading = 'E'
                nextfound = True
            
            elif heading == 'W' and nextpos == 'L':
                heading = 'N'
                nextfound = True
            
            elif heading == 'W' and nextpos == 'F':
                heading = 'S'
                nextfound = True
            
            if nextpos == 'S':
                startfound = True
                print("loop found")
                print(steps)
                
            if nextfound:
                #print(nextpos + " - heading: " + heading)
                nextstep = compassheading(heading)
                next = (next[0]+nextstep[0], next[1]+nextstep[1])
                
                #print("nextstep: " + str(next) + " - nextheading: " + heading)
                
                #print(next)   
                #input("next")
            else:
                break

#print(map)
print(start)
print("day 10 - 1")
result = (steps-1)/2
print(result)
print()
