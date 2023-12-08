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
