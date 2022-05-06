# Just a small code snippet to get the number of dice thrown
def normalandspecial(dicelist, specialdicelist):
    diceamount = 0
    if dicelist:
        for i in range(int(len(dicelist) / 2)):
            diceamount += dicelist[i * 2]
    if specialdicelist:
        for i in range(int(len(specialdicelist) / 2)):
            diceamount += specialdicelist[i * 2]
    return diceamount
