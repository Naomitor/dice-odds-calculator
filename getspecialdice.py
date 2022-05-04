import sys

def differentdiceallatoncemultiple():

    # What's to do as user
    print("Please input the dice set, to exit type end:")

    # Set dicepart False for loop then get how many dice the user wants to throw or exit the program
    dicepart = False
    while not dicepart:
        dicepart = input()
        # Exit program with end
        if dicepart == "end":
            sys.exit("Bye")

    # Empty dicelist if error occurred
    dicelist = []
    # Error protection if any false input was given
    try:
        # Look if d or numbers are missing
        dpoint = dicepart.find("d")
        if dpoint == -1:
            print("You forgot the d ;)")
        else:
            # Splitting the string into a list for further processing
            for i in range(dicepart.count("d")):
                # Find the next d for spacing the numbers
                dpoint = dicepart.find("d")
                # Set diceamount to the numbers out of dicepart until the point of the next d
                diceamount = int(dicepart[:dpoint])
                # Remove the numbers and next d out of dicepart
                dicepart = dicepart[dpoint+1:]
                # Find the space for spacing the next numbers
                spacepoint = dicepart.find(" ")
                # Test for end of dicepart if not set to the point of space else set everything and fill in dicelist
                if spacepoint >= 1:
                    diceeyes = int(dicepart[:spacepoint])
                else:
                    diceeyes = int(dicepart[:])
                    dicelist.append(diceamount)
                    dicelist.append(diceeyes)
                    break
                # Remove the numbers and next space out of dicepart
                dicepart = dicepart[spacepoint+1:]
                # Fill in dicelist
                dicelist.append(diceamount)
                dicelist.append(diceeyes)
    except (IndexError, ValueError):
        print("That did not work. Please check for typos")

    # Return dicelist to the caller function
    return dicelist