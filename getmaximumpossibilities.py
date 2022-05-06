# Just a little snippet that returns all possibilities
def normalandspecial(dicelist, specialdicelist):
    possibilities = 1
    if dicelist:
        for i in range(int(len(dicelist) / 2)):
            possibilities *= (dicelist[i * 2 + 1] ** dicelist[i * 2])
    if specialdicelist:
        for i in range(int(len(specialdicelist) / 2)):
            possibilities *= (len(specialdicelist[i * 2 + 1]) ** specialdicelist[i * 2])
    return possibilities
