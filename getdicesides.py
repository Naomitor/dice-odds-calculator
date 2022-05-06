# A small code snippet that fills a list with dice sides * dice amount
def normalandspecial(dicelist, specialdicelist):
    dicesideslist = []
    specialdicesideslist = []
    inbetweenlist = []
    if dicelist and specialdicelist:
        for i in range(int(len(specialdicelist) / 2)):
            for j in range(specialdicelist[i * 2]):
                specialdicesideslist.append(specialdicelist[i * 2 + 1])
        for i in range(int(len(dicelist) / 2)):
            for j in range(dicelist[i * 2]):
                for k in range(dicelist[i * 2 + 1]):
                    inbetweenlist.append(k + 1)
                specialdicesideslist.append(inbetweenlist)
                inbetweenlist = []
    if dicelist:
        for i in range(int(len(dicelist) / 2)):
            for j in range(dicelist[i * 2]):
                dicesideslist.append(dicelist[i * 2 + 1])
    if specialdicelist:
        for i in range(int(len(specialdicelist) / 2)):
            for j in range(specialdicelist[i * 2]):
                specialdicesideslist.append(specialdicelist[i * 2 + 1])

    return dicesideslist, specialdicesideslist
