f = open("2.txt", "r")
input = f.read().splitlines() #read lines to list
readcount = 0 #count lines read
cal = [] #Array to hold sums
tempcal = 0 #temp var to calculate elf total cal
input_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
sum = 0
sum2 = 0

while readcount < len(input) :
    
    r = 0
    g = 0
    b = 0
    
    inputtxt = input[readcount]
    
    print(inputtxt)
    
    iso = inputtxt.split(':')
    
    game, gamenostr = iso[0].split(' ')
    gameno = int(gamenostr.strip())
    games = iso[1].split(';')
    valid = True
    gameslen = len(games)
    gamecounter = 0
    for game in games:
        cubes = game.split(',')
        for cube in cubes:
            #print(cube)
            quantity, color = cube.strip().split(' ')
            if color == 'blue' and int(quantity) > 14:
                valid = False

            if(color == 'blue' and int(quantity) > b):
                b = int(quantity)
            
            if color == 'green' and int(quantity) > 13:
                valid = False

            if(color == 'green' and int(quantity) > g):
                g = int(quantity)
            
            if color == 'red' and int(quantity) > 12:
                valid = False

            if(color == 'red' and int(quantity) > r):
                r = int(quantity)
                
        gamecounter += 1
    
    if(valid):
        sum += gameno
        #print(gameno)
    
    #print(r)
    #print(g)
    #print(b)
    
    sum2 += r*g*b
    
    readcount += 1 #increment line to read
    


print("day 2 - 1")
print(sum)
print("day 2 - 2")
print (sum2)