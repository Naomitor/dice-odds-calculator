# Import time for tracking script run time and getnumerbers.py
import getnumbers

# Welcome text
print("With this little tool you can calculate the mean throw of any dice.")
print("First input the set of dice you want to throw like 2d6, ")
print("where 2 is the number of dice you want to throw and 6 is the highest number of eyes on the dice.")
print("If you have different sets that you want to throw together, ")
print("enter the first set of same eyes press space, then repeat for the others.")
print("Like this: 12d4 2d6 6d8")
print("Once you are finished press enter, to exit type end.")

# While loop to make the program repeatable
circle = True
while circle:

    # Call the get numbers function for the dice list
    dicelist = getnumbers.differentdiceallatoncemultiple()

    if not dicelist:
        continue

    # Set variables and calculate mean dmg enter resulttext for better user-visualisation
    result = 0
    resulttext = ""
    for i in range(int(len(dicelist)/2)):
        result += (((dicelist[i*2+1]+1)/2) * dicelist[i*2])
        resulttext = resulttext + str(dicelist[i*2]) + "d" + str(dicelist[i*2+1]) + ", "

    # remove last ", "
    resulttext = resulttext[0:len(resulttext) - 2]

    # Print result
    print("The mean throw of " + resulttext + " is: " + str(result))
    print("Lets go again!")
