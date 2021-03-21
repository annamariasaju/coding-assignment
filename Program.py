inputFile =open("sample_input.txt","r")
outputFile = open("output.txt","w+")

listGoodies={}
finalList = []
tempList=[]

#Function to find the difference
def findPriceDifference(pricesSeperatedList, totalEmployees, listLength):
    result = 2147483647
    for i in range(listLength - totalEmployees + 1):
        result = int(min(result, pricesSeperatedList[i + totalEmployees - 1] - pricesSeperatedList[i]))

    return result  
    



for i in inputFile:
    fullColonIndex = i.index(":")
    listGoodies[i[:fullColonIndex]]=i[fullColonIndex+1:].strip()
pricesSeperatedList = list(map(int, listGoodies.values()))
pricesSeperatedList.sort()

listLength = len(pricesSeperatedList)
totalEmployees=int(input("Enter number of employees: "))

PriceDifference = findPriceDifference(pricesSeperatedList, totalEmployees, listLength)
print(PriceDifference)

for i in range(listLength):
    for j in range(listLength):
        if(pricesSeperatedList[i] - pricesSeperatedList[j] == PriceDifference):
                upperBound = pricesSeperatedList.index(pricesSeperatedList[i])
                loweBound = pricesSeperatedList.index(pricesSeperatedList[j])

for i in range(loweBound, upperBound + 1, 1):
    tempList.append(pricesSeperatedList[i])



tempList.sort(reverse=True)
print(tempList)


cnt=0
for key,value in listGoodies.items():
    pricesSeperatedList[cnt]
    print(value)
    if int(value)in tempList and cnt<totalEmployees:
        str1=key+": "+value
        #preparing  list for output
        finalList.append(str1)
        cnt+=1
        print(str1)
#writing to output file
outputFile.write("The goodies selected for distribution: ")

outputFile.write("\n")

for i in finalList:
    outputFile.write(i)
    outputFile.write("\n")
outputFile.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(PriceDifference))


inputFile.close()
outputFile.close()