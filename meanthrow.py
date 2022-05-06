# Import time for tracking script run time and getnumerbers.py
import getdice

# While loop to make the program repeatable
circle = True
while circle:

    # Call the get numbers function for the dice list
    dicelist, specialdicelist, userinfo = getdice.listswitheverything()

    if not dicelist and not specialdicelist:
        print("There seems to be a problem")

    else:
        # Set variable
        result = 0
        resulttext = ""

        # Calculate mean throw for standard sets and add it to result
        if dicelist:
            for i in range(int(len(dicelist) / 2)):
                result += (((dicelist[i * 2 + 1] + 1) / 2) * dicelist[i * 2])

        # Calculate mean throw for special sets and add it to result
        if specialdicelist:
            for i in range(int(len(specialdicelist) / 2)):
                eyesum = 0
                for j in range(int(len(specialdicelist[i * 2 + 1]))):
                    eyesum += specialdicelist[i * 2 + 1][j]
                result += ((eyesum / int(len(specialdicelist[i * 2 + 1]))) * specialdicelist[i * 2])

        # Print result
        print("The mean throw of " + userinfo + " is: " + str(result))
        print("Lets go again!")