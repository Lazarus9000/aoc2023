f = open("4.txt", "r")
input = f.read().splitlines() #read lines to list
readcount = 0 #count lines read
sum = 0

while readcount < len(input) :
    inputtxt = input[readcount]
    cards = inputtxt.split("|")
    #print(cards)
    winners = []
    haves = []
    winners = cards[0].split()
    haves = cards[1].split()
    #print(winners)
    #print(haves)
    point = 0
    for winner in winners:
        for have in haves:
            if have == winner:
                #print(have)
                if point == 0:
                    point = 1
                else:
                    point = point*2
    
    sum += point
    
    readcount += 1         
            
print("day 4 - 1")
print(sum)

readcount = 0 #count lines read
sum = 0
newinput = input

#print(len(newinput))
points = []
for i in range(len(newinput)):
    points.append(1)

while readcount < len(newinput) :
    inputtxt = newinput[readcount]
    cards = inputtxt.split("|")
    #print(cards)
    winners = []
    haves = []
    winners = cards[0].split()
    haves = cards[1].split()
    #print(winners)
    #print(haves)
    point = 0
    for winner in winners:
        for have in haves:
            if have == winner:
               #print(have)
                point += 1
    
    #print(point)
    tempinput = newinput[0:readcount+1]
    tempinput = tempinput + newinput[readcount+1:readcount+1+point] + newinput[readcount+1:readcount+1+point]
    tempinput = tempinput + newinput[readcount+1+point:]
    #print(tempinput)
    #newinput = tempinput
    #print(input[readcount+1:readcount+point])    
    #print(point)
    
    for j in range(readcount+1,readcount+point+1):
        #print("j: " + str(j) + " - i: " + str(i))
        #print(points[j])
        points[j] = points[j]+1
        #print("adding")
            
        for i in range(points[readcount]-1):
            #print("j: " + str(j) + " - i: " + str(i))
            #print(points[j])
            points[j] = points[j]+1
            #print("adding")
    #print(points)
    
    readcount += 1         

#print(points)
sum2 = 0 
for p in points:
    sum2 += p
    

print("day 4 - 2")
print(sum2)