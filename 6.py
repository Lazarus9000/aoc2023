f = open("6.txt", "r")
input = f.read() #read lines to list
#input = "Time:      7  15   30\nDistance:  9  40  200"
inputs = input.split("\n")

times = []
distances = []
sum = 0

for input in inputs:
    fields = input.split()
    print(fields)
    if(fields[0] == "Time:"):
        times = fields[1:]
        times = list(map(int, times))
        print(times)
    
    if(fields[0] == "Distance:"):
        distances = fields[1:]
        distances = list(map(int, distances))
        print(distances)
        
beats = []
for i in range(len(times)):
    beat = 0
    for j in range(times[i]):
        travel = j*(times[i]-j)
        #print(travel)
        if travel > distances[i]:
            beat += 1
    #print(beats)
    beats.append(beat)
    
for beat in beats:
    if sum == 0:
        sum = beat
    else:
        sum = sum * beat 
print("day 6 - 1")
print(sum)
print()

times = []
distances = []
sum = 0

for input in inputs:
    fields = input.split()
    #print(fields)
    if(fields[0] == "Time:"):
        times = fields[1:]
        times = list(map(int, times))
        #print(times)
    
    if(fields[0] == "Distance:"):
        distances = fields[1:]
        distances = list(map(int, distances))
        #print(distances)
        
beats = []

laptime = ""
for time in times:
    laptime = laptime + str(time)

print(laptime)
laptime = int(laptime)
lapdistance = ""
for distance in distances:
    lapdistance = lapdistance + str(distance)

print(lapdistance)
lapdistance = int(lapdistance)

beat = 0
for j in range(laptime):
    travel = j*(laptime-j)
    #print(travel)
    if travel > lapdistance:
        beat += 1
#print(beats)
#beats.append(beat)

print("day 6 - 2")
print(beat)
