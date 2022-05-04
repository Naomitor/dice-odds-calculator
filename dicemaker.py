x = 3
y = 20

dicethrowerlist = []
dicelist = []
counterdicesides = 0

# Fill the dice thrower with 1s to set the starting throw
for i in range(x):
    dicethrowerlist.append(1)

# Do the loop for diceeyes^diceamount
for i in range(y**x):

    # Reset result for next dice value and add all dice throws to it. Append to the whole dice list
    result = 0
    for j in range(x):
        result += dicethrowerlist[j]
    dicelist.append(result)
    counterdicesides += 1

    # Test for the range of dice amount if the maximum side value has been reached, if so set the position in the range to 1 and trigger the overflow so that the
    # next position that is not on its maximum side can be increased by one
    for j in range(x):
        if dicethrowerlist[j] == y:
            dicethrowerlist[j] = 1
            overflow = True
        else:
            dicethrowerlist[j] += 1
            overflow = False
            break

dicelist.sort()
print(dicelist)
print(counterdicesides)
print(y**x)
