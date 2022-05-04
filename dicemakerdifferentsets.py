import timeit
import getnumbers

# Initiate the vars and lists and get the dice set list
diceinput = getnumbers.differentdiceallatoncemultiple()
dicethrowerlist = []
looptimes = 1
dicelist = []
diceamount = 0
dicesides = []
#counterdicesides = 0

# Set start time
starttime = timeit.default_timer()

# Fill the dice thrower with 1s to set the starting throw and calculate the amount the loop needs to be run by calculating each amount of dice
for i in range(int(len(diceinput)/2)):
    looptimes *= (diceinput[i*2+1] ** diceinput[i*2])
    diceamount += diceinput[i*2]
    for j in range(diceinput[i*2]):
        dicesides.append(diceinput[i*2+1])
        dicethrowerlist.append(1)


# Do the loop for the amount of dice sides^dice amount
for i in range(looptimes):

    # Reset result for next dice value and add all dice throws to it. Append to the whole dice list
    result = 0
    for j in range(diceamount):
        result += dicethrowerlist[j]
    dicelist.append(result)
    #counterdicesides += 1

    # Test for the range of dice amount if the maximum side value has been reached, if so set the position in the range to 1 and trigger the overflow so that the
    # next position that is not on its maximum side can be increased by one
    for j in range(diceamount):
        if dicethrowerlist[j] == dicesides[j]:
            dicethrowerlist[j] = 1
            overflow = True
        else:
            dicethrowerlist[j] += 1
            overflow = False
            break

# Set ending time and calculate time needed
endtime = timeit.default_timer()
time = endtime - starttime

dicelist.sort()
#print(dicelist)
#print(counterdicesides)
print("Amount of possibilities calculated " + str(looptimes) + " in {:.2f} seconds".format(time))
