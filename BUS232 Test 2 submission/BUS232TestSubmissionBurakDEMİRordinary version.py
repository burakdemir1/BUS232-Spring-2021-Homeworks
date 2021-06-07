def getShares():
    sharesList = []
    share = int(input("Please enter the number of shares: "))
    while share != 0:
        sharesList.append(share)
        share = int(input("Please enter the number of shares: "))
    sharesList.sort(reverse = True)
    return sharesList


shareList = getShares()
numOfShareHolders = len(shareList)
totalShares = sum(shareList)
neededShare = int (sum(shareList) / 2) + 1

neededShareHolders = 0
sumShares = 0
while neededShare > sumShares:
    sumShares += shareList[neededShareHolders]
    neededShareHolders += 1 



totalstr = "Total Share: " + str(totalShares)
needstr = "Need Share: " + str(neededShare)
needshareholdersstr = "Needed Shareholders: " + str(neededShareHolders)
totalshareholdersstr = "Total Shareholders: " + str(numOfShareHolders)
finalstr = totalstr + "\n" + needstr + "\n" + totalshareholdersstr + "\n" + needshareholdersstr 

print(finalstr)
