def median(numList):
    print sorted(numList)
    numList = sorted(numList)
    print numList
    lengthOfList = len(numList)
    if lengthOfList % 2 == 0:
        return (numList[int(lengthOfList/2.0)] + numList[int(lengthOfList/2.0 - 1)]) / 2.0
    else:
        return numList[int(round(lengthOfList/2,0))]

print median([4,5,5,4])
