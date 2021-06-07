def numberOfNeededShareHolders(myShares, need):
        numOfneededShareHolders = 0
        totalShareSoFar = 0
        while need > totalShareSoFar:
            totalShareSoFar += myShares[numOfneededShareHolders]
            numOfneededShareHolders += 1
        return numOfneededShareHolders

def printToTxt(myShares,need,total):
    stringTotal = "Total Share: " + str(total)
    stringNeed = "Need Share: " + str(need)
    stringNeedShareHolders = "Needed Shareholders: " + str(numberOfNeededShareHolders(myShares,need))
    endString = stringTotal + "\n" + stringNeed + "\n" + stringNeedShareHolders 
    file = open("output.txt","w") 
    file.write(endString)
    file.close

myShares = []
total = 0
totalNumOfShare = 0
myShare = int(input("Please enter the number of shares: "))

while myShare != 0:
    myShares.append(myShare)
    totalNumOfShare += 1
    myShare = int(input("Please enter the number of shares: "))

    
myShares.sort(reverse = True)

for i in myShares:
    total += i

need = int (total / 2) + 1

numOfPeople = numberOfNeededShareHolders(myShares,need)
print("Total Share: " + str(total))
print("Need Share: " + str(need))
print("Total Shareholders: " + str(totalNumOfShare))
print("Needed Shareholders: " + str(numOfPeople))

printToTxt(myShares,need,total)