# A small code snippet that returns the maximum side of a dice
def special(specialdicesideslist):
    specialdicesidesiterationlist = []
    for i in range(len(specialdicesideslist)):
        specialdicesidesiterationlist.append(len(specialdicesideslist[i]) - 1)
    return specialdicesidesiterationlist
