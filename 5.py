f = open("5.txt", "r")
input = f.read() #read lines to list
inputs = input.split("\n\n")

mapping = []
seeds = []
for input in inputs:
    fields = input.split()
    #print(fields)
    if(fields[0] == "seeds:"):
            seeds = fields[1:]
            seeds = list(map(int, seeds))
            print(seeds)
    else:
        mapping = []
        maps = input.split("\n")
        print(maps[0])
        for j in range(len(maps[1:])):
            mapping.append(maps[j+1])
        print(mapping)
        
        seedmap = [0] * len(seeds)
        
        for s in range(len(seeds)):
            for mapvals in mapping:
                values = mapvals.split()
                values = list(map(int, values))
                #print(str(values[1]))
                if seeds[s] >= values[1] and values[1]+values[2] > seeds[s] and seedmap[s]!=-1:
    
                    seeds[s] = int(seeds[s]) - (values[1]-values[0])
                    seedmap[s] = -1
                    #print("value map! " + str(seeds[s]) + " - " + mapvals)
    print(seeds)
            
print("day 5 - 1")

minseed = seeds[0]
for seed in seeds:
    if seed < minseed:
        minseed = seed

print(minseed)


mapping = []
seeds = []
initseeds = []
mapz = []
for input in inputs:
    fields = input.split()
    #print(fields)
    if(fields[0] == "seeds:"):
            initseeds = fields[1:]
            initseeds = list(map(int, initseeds))
            print(initseeds)
            s = 0
            #while s < len(initseeds):
                #for i in range(initseeds[s],initseeds[s]+initseeds[s+1]):
                    #print(i)
                    #seeds.append(i)
                #s = s + 2
            #print(seeds)
    else:
        mapping = []
        maps = input.split("\n")
        #print(maps[0])
        for j in range(len(maps[1:])):
            mapping.append(list(map(int,maps[j+1].split())))
        #print(mapping)
        mapz.append(mapping)

#print(mapz)
minseeds = []
z = 4
while z < len(initseeds):
    seeds = []
    #seeds.append(list(range(initseeds[z], initseeds[z]+initseeds[z+1])))
    
    seedrange = range(initseeds[z],initseeds[z]+initseeds[z+1])
    
    for i in seedrange:    
        seeds.append(i)

    print(str(z) + " - " + str(len(initseeds)) + " - " + str(initseeds[z]) + " - " + str(initseeds[z]+initseeds[z+1]))
    #print(seeds)
    
    
    for mapping in mapz:
        seedmap = [0] * len(seeds)
        print("map: " + str(mapping))
        
        for s in range(len(seeds)):
            for mapvals in mapping:
                #values = mapvals.split()
                #print(values)
                #values = list(map(int, values))
                #print(str(values[1]))
                if seedmap[s] != -1:
                    if seeds[s] >= mapvals[1]:
                        if seeds[s] < mapvals[1]+mapvals[2]:
                            
                            seeds[s] = int(seeds[s]) - (mapvals[1]-mapvals[0])
                            seedmap[s] = -1
                    #print("value map! " + str(seeds[s]) + " - " + mapvals)
                
    minseed = seeds[0]
    for seed in seeds:
        if seed < minseed:
            minseed = seed
    minseeds.append(minseed)
    print(minseeds)
    z = z + 2 
    #print(seeds)
    
print("day 5 - 2")

minseed = minseeds[0]
for seed in minseeds:
    if seed < minseed:
        minseed = seed

print(minseed)