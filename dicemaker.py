import timeit
import getdice
import getdiceamount
import getmaxsides
import getmaximumpossibilities
import getdicesides


def dicemaker():
    # Call the get numbers function for the dice list
    dicelist, specialdicelist, userinfo = getdice.listswitheverything()

    # Initiate variables
    dicethrowerlist = []
    alldicepossibilitieslist = []
    specialdicesidesiterationlist = []
    dicethroweriterationlist = []
    # counterdicesides = 0

    # Set start time
    starttime = timeit.default_timer()

    diceamount = getdiceamount.normalandspecial(dicelist, specialdicelist)
    maximumpossibilities = getmaximumpossibilities.normalandspecial(dicelist, specialdicelist)
    dicesideslist, specialdicesideslist = getdicesides.normalandspecial(dicelist, specialdicelist)
    specialdicesidesnumberiterationlist = getmaxsides.special(specialdicesideslist)

    # If dicelist is full it gets converted to special dice to work with this special dice maker
    if specialdicesideslist:
        # Fill the dice thrower with the position 0 of the custom dice to set the starting throw
        for i in range(diceamount):
            dicethrowerlist.append(specialdicesideslist[i][0])
            specialdicesidesiterationlist.append(1)
            dicethroweriterationlist.append(0)

        # Do the loop for dicesides^diceamount
        for i in range(maximumpossibilities):

            # Reset result for next dice value and add all dice throws to it. Append to the whole dice list
            result = 0
            for j in range(diceamount):
                result += dicethrowerlist[j]
            alldicepossibilitieslist.append(result)
            # counterdicesides += 1

            # Test for the range of dice amount if the maximum side value has been reached, if so set the position to 0 and trigger the overflow so that the
            # next position that is not on its maximum side can be increased by one
            for j in range(diceamount):
                if dicethroweriterationlist[j] == specialdicesidesnumberiterationlist[j]:
                    dicethrowerlist[j] = specialdicesideslist[j][0]
                    specialdicesidesiterationlist[j] = 1
                    dicethroweriterationlist[j] = 0
                    overflow = True
                else:
                    dicethrowerlist[j] = specialdicesideslist[j][specialdicesidesiterationlist[j]]
                    specialdicesidesiterationlist[j] += 1
                    dicethroweriterationlist[j] += 1
                    overflow = False
                    break

    # Only for dicelist if specialdicelist is empty
    else:
        # Fill the dice thrower with 1s to set the starting throw
        for i in range(diceamount):
            dicethrowerlist.append(1)

        # Do the loop for dicesides^diceamount
        for i in range(maximumpossibilities):

            # Reset result for next dice value and add all dice throws to it. Append to the whole dice list
            result = 0
            for j in range(diceamount):
                result += dicethrowerlist[j]
            alldicepossibilitieslist.append(result)
            # counterdicesides += 1

            # Test for the range of dice amount if the maximum side value has been reached, if so set the position to 0 and trigger the overflow so that the
            # next position that is not on its maximum side can be increased by one
            for j in range(diceamount):
                if dicethrowerlist[j] == dicesideslist[j]:
                    dicethrowerlist[j] = 1
                    overflow = True
                else:
                    dicethrowerlist[j] += 1
                    overflow = False
                    break

    # Set ending time and calculate time needed
    endtime = timeit.default_timer()
    time = endtime - starttime

    # print(alldicepossibilitieslist)
    alldicepossibilitieslist.sort()
    # print(alldicepossibilitieslist)
    # print(len(alldicepossibilitieslist))
    # print(dicelist)
    # print(counterdicesides)
    print("Amount of possibilities calculated " + str(maximumpossibilities) + " in " + str(format(time, '.2f')) + " seconds")

    return alldicepossibilitieslist, maximumpossibilities
