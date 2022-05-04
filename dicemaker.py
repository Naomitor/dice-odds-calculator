import timeit
import getnumbers

# Call the get numbers function for the dice list
diceamount, diceeyes = getnumbers.getnumbers()

dicethrowerlist = []
dicelist = []
#counterdicesides = 0

# Set start time
starttime = timeit.default_timer()

# Fill the dice thrower with 1s to set the starting throw
for i in range(diceamount):
    dicethrowerlist.append(1)

# Do the loop for diceeyes^diceamount
for i in range(diceeyes**diceamount):

    # Reset result for next dice value and add all dice throws to it. Append to the whole dice list
    result = 0
    for j in range(diceamount):
        result += dicethrowerlist[j]
    dicelist.append(result)
    #counterdicesides += 1

    # Test for the range of dice amount if the maximum side value has been reached, if so set the position in the range to 1 and trigger the overflow so that the
    # next position that is not on its maximum side can be increased by one
    for j in range(diceamount):
        if dicethrowerlist[j] == diceeyes:
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
print("Amount of possibilities calculated " + str(diceeyes**diceamount) + " in " + str(time))
