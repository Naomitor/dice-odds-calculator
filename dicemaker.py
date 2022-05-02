x = 3
y = 4

dicethrowerlist = []
dicelist = []
didreset = True
loop = False
stop = False
counterdicesides = 0
dice = 1

# Fill the dice thrower with 1s to set the starting throw
for i in range(x):
    dicethrowerlist.append(1)

for i in range(y**x-x):

    # Check if dicethrowerlist has reached the max eyes on the first dice
    if dicethrowerlist[0] == y:
        dicethrowerlist[0] = 1

        # Resets all dicethrowerlist values that are y to 1
        for j in range(x):
            if dicethrowerlist[j] != y:
                continue
            else:
                dicethrowerlist[j] = 1

        # Find the last value of dicethrowerlist that is not 1 to increase
        dicethrowerlist.reverse()
        for j in range(1, x):
            if dicethrowerlist[j] != 1:
                dicethrowerlist[j] += 1
                break
            # ?
            elif dice == x:
                stop = True
                break
            # Set the new highest dicethrowerlist value to 2 so the program can continue
            else:
                dicethrowerlist[j] = 2
                dice += 1
                break
        dicethrowerlist.reverse()

    # Stop the program for last run only
    if stop:
        break

    # Calculate first result after setting 1s
    if dicethrowerlist[0] == 1:
        result = 0
        for j in range(x):
            result += dicethrowerlist[j]
        dicelist.append(result)
        counterdicesides += 1

    # Increase the next list value by 1
    for j in range(x):
        if dicethrowerlist[j] == y:
            continue
        else:
            dicethrowerlist[j] += 1
            break

    # Reset result for next dice value and add all dice throws to it. Append to the whole dice list
    result = 0
    for j in range(x):
        result += dicethrowerlist[j]
    dicelist.append(result)
    counterdicesides += 1

#dicelist.sort()
print(dicelist)
print(counterdicesides)
print(y**x)