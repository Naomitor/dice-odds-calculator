# Calculates the chance to get any given value out of a die
import dicemaker

# Initiate variables
loop = True
minimum = 0
possibilities = 0

# Get all possible throws
alldicepossibilitieslist, maximumpossibilities = dicemaker.dicemaker()

print("The result are between: " + str(alldicepossibilitieslist[0]) + "-" + str(alldicepossibilitieslist[-1]) + ". What do you need at least?:")
while loop:
    try:
        minimum = int(input())
        loop = False
    except ValueError:
        print("That's no number")

counter = minimum
for i in range(alldicepossibilitieslist[-1] - minimum + 1):
    possibilities += alldicepossibilitieslist.count(counter)
    counter += 1

print(format((possibilities / maximumpossibilities) * 100, '.2f') + "%")
