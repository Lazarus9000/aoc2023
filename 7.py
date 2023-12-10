f = open("7.txt", "r")
input = f.read() #read lines to list
#input = "Time:      7  15   30\nDistance:  9  40  200"
inputs = input.split("\n")

hands = input.split()[::2]
bets = input.split()[1::2]
sum = 0

def fiveofakind(hand):
    card = hand[0]
    five = True
    for cards in hand:
        if cards != card:
            five = False
    
    return five

def xofakind(hand, count):
    countsum = []
    countresult = False
    
    for i in range(len(hand)):
        countsum.append(0)
        for card in hand:
            if hand[i] == card:
                countsum[i] += 1
    
    for card in countsum:
        if card == count:
            countresult = True
    
    return countresult

def ishouse(hand):
    if xofakind(hand, 2) and xofakind(hand, 3):
        return True
    else:
        return False

def twopairs(hand):
    countsum = []
    countresult = False
    
    for i in range(len(hand)):
        countsum.append(0)
        for card in hand:
            if hand[i] == card:
                countsum[i] += 1
    
    #print(countsum)
    countpairs = 0
    for card in countsum:
        if card == 2:
            countpairs += 1
    
    #print(countpairs)
    
    if countpairs == 4:
        countresult = True
    
    return countresult

def cardval(card):
    #check if numeric
    result = 0
    if card.isnumeric():
        result = int(card)
    elif card == "T":
        result = 10
    elif card == "J":
        result = 11
    elif card == "Q":
        result = 12
    elif card == "K":
        result = 13
    elif card == "A":
        result = 14
    return result

def sorthands(hands):
    
    if len(hands) == 1:
        print("no sort")
        #print(hands)
        combind = [hands,bets]
        return hands

    #print(hands)
    sortedhands = []
    winner = False
    
    
    
    if len(hands) > 0:
        sortedhands.append(hands[0])
        for i in range(1, len(hands)):
            winner = False
            for j in range(len(hands)):
                if i != j and j < len(sortedhands):
                    #print(str(hands[i][0]) + " v " + str(sortedhands[j][0]))
                    for x in range(len(hands[i][0])):
                        
                        carda = hands[i][0][x]
                        cardb = sortedhands[j][0][x]
                        #print(carda + " vs " + cardb)
                        if carda == cardb:
                            continue
                        
                        if cardval(carda) > cardval(cardb):
                            
                            #print(str(hands[i]) + " - winner")
                            
                            break
                        else:
                            #print(str(sortedhands[j]) + " - winner")
                            sortedhands.insert(j,hands[i])
                            winner = True
                            break
                    
                    if(winner):
                        break
            if(not(winner)):
                #print("largest hand found, adding to end")
                sortedhands.append(hands[i])
                winner = True
                
                
            
            #for hand in sortedhands:
                #print(hand)
            
    #for i in range(len(hands)):
    #    if sortedhands[0].count(hands[i][0]) == 0:
    #        sortedhands.append(hands[i])
            

    #print(sortedhands)
    return sortedhands

fives = []
fours = []
house = []
threes = []
doubles = []
twos = []
highs = []
print(hands)

for i in range(len(hands)):
    #print(i)
    #five of a kind
    #print(hands[i])
    if(xofakind(hands[i],5)):
        fives.append([hands[i],bets[i]])
        #print("5")
    elif (xofakind(hands[i],4)):
        fours.append([hands[i],bets[i]])
        #print("4")
    elif ishouse(hands[i]):
        house.append([hands[i],bets[i]])
    elif (xofakind(hands[i],3)):
        threes.append([hands[i],bets[i]])
        #print("3")
    elif (twopairs(hands[i])):
        doubles.append([hands[i],bets[i]])
        #print("22")
    elif (xofakind(hands[i],2)):
        twos.append([hands[i],bets[i]])
        #print("2")
    else:
        highs.append([hands[i],bets[i]])
        #print("1")
    
    #print()






#Combine lists after ordering
#for hand in sorthands(highs):
#    print(hand)
sortedhands = sorthands(highs) + sorthands(twos) + sorthands(doubles) + sorthands(threes) + sorthands(house) + sorthands(fours) + sorthands(fives)
for hand in sortedhands:
    print(hand)
counter = 1
#sortedhands()
for hand in sortedhands:
    score = int(hand[1])*counter
    sum = sum + score
    counter += 1
    #print(str(hand) + " - " + str(score))

#Score

#Summarize


print("day 7 - 1")
print(sum)
print()
