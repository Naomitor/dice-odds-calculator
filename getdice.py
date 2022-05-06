# Import dependencies
import sys


def listswitheverything():
    # What's to do as user
    print("Please input the dice set, to exit type end:")

    # Initiate vars
    dicelist, specialdicelist, userinfo = [], [], ""
    loopbreak = False
    # loop for error protection
    while not loopbreak:

        # Get how many dice the user wants to throw or exit the program
        dicepart = input()
        # Exit program with end
        if dicepart == "end":
            sys.exit("Bye")
        userinfo = dicepart

        # Empty dicelist if error occurred
        dicelist = []
        specialdicelist = []
        diceeyeslist = []

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
                    # Find the next open brace (
                    bracepoint = dicepart.find("(")
                    # If the special dice is the next set this will filter it out of the string dicepart into the list specialdicelist.
                    if bracepoint - dpoint == 1:
                        # Append the dice amount to the list
                        specialdicelist.append(int(dicepart[:dpoint]))
                        # Remove the amount and d from dicepart
                        dicepart = dicepart[dpoint + 2:]
                        # Find the next space
                        spacepoint = dicepart.find(" ")
                        # If spacepoint is equal or larger than 1 filter all eyes into the diceeyeslist and append that to specialdicelist
                        if spacepoint >= 1:
                            for j in range(int(len(dicepart[:spacepoint]) / 2)):
                                diceeyeslist.append(int(dicepart[j * 2]))
                            specialdicelist.append(diceeyeslist)
                            # Remove the part from spacepoint
                            dicepart = dicepart[spacepoint + 1:]
                        # Else filter the rest of dicepart into the diceeyeslist and append that to the specialdicelist
                        else:
                            for j in range(int(len(dicepart[:]) / 2)):
                                diceeyeslist.append(int(dicepart[j * 2]))
                            specialdicelist.append(diceeyeslist)
                            break
                    # If it is a normal set this filters it out of the input string and appends it to dicelist
                    else:
                        # Add the dice amount to the dice list to the point of the next d
                        dicelist.append(int(dicepart[:dpoint]))
                        # Remove the numbers and next d out of dicepart
                        dicepart = dicepart[dpoint + 1:]
                        # Find the next space
                        spacepoint = dicepart.find(" ")
                        # Test for the end of dicepart by searching for space, if found append everything between it and 0 to the dicelist
                        # and delete this part out of dicepart,if no space can be found anymore the rest of dicepart is copied into dicelist and the loop gets broken.
                        if spacepoint >= 1:
                            dicelist.append(int(dicepart[:spacepoint]))
                            dicepart = dicepart[spacepoint + 1:]
                        else:
                            dicelist.append(int(dicepart[:]))
                            break
                loopbreak = True
        except (IndexError, ValueError):
            print("That did not work. Please check for typos")

    # print(dicelist, specialdicelist)
    # Return dicelist with normal sets, specialdicelist with the user defined set and the userinfo with input dice sets to the caller function
    return dicelist, specialdicelist, userinfo
