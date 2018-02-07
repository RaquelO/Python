#This programs reads a supplied text file, hurricanes.txt, that contains monthly rainfall data for six years.
#Program reads the data from this text file to generate a CSV file which calculates
#and displays the average for the month across all six years.

#Open the provided file
stormData = open("hurricanes.txt", "r")

#create list variables for the years, and each month
stormYears = []
stormsMay = []
stormsJune = []
stormsJuly = []
stormsAug = []
stormsSept = []
stormsOct = []
stormsNov = []
stormsDec = []

#use a for loop to read and tokenize each line of the file
for line in stormData :
  tokens = line.rstrip("\n").split(":")
  if len(tokens) == 1 :
    stormYears.append(tokens[0])
  else :#save data for years and months into their own list type variables
    if tokens[0] == "May" :
      stormsMay.append(tokens[1])
    elif tokens[0] == "Jun" :
      stormsJune.append(tokens[1])
    elif tokens[0] == "Jul" :
      stormsJuly.append(tokens[1])
    elif tokens[0] == "Aug" :
      stormsAug.append(tokens[1])
    elif tokens[0] == "Sep" :
      stormsSept.append(tokens[1])
    elif tokens[0] == "Oct" :
      stormsOct.append(tokens[1])
    elif tokens[0] == "Nov" :
      stormsNov.append(tokens[1])
    elif tokens[0] == "Dec" :
      stormsDec.append(tokens[1])

#calculate average for each month
sumMay = 0
for i in stormsMay :
  sumMay = sumMay + int(i)
avgMay = str(sumMay/len(stormsMay))
#print("sum is: ",sumMay)
#print("average is: ",format(avgMay, ".2f"))

sumJune = 0
for i in stormsJune :
  sumJune = sumJune + int(i)
avgJune = str(sumJune/len(stormsJune))

sumJuly = 0
for i in stormsJuly :
  sumJuly = sumJuly + int(i)
avgJuly = str(sumJuly/len(stormsJuly))

sumAug = 0
for i in stormsAug :
  sumAug = sumAug + int(i)
avgAug = str(sumAug/len(stormsAug))

sumSept= 0
for i in stormsSept :
  sumSept = sumSept + int(i)
avgSept = str(sumSept/len(stormsSept))

sumOct = 0
for i in stormsOct :
  sumOct = sumOct + int(i)
avgOct = str(sumOct/len(stormsOct))

sumNov = 0
for i in stormsNov :
  sumNov = sumNov + int(i)
avgNov = str(sumNov/len(stormsNov))

sumDec = 0
for i in stormsDec :
  sumDec = sumDec + int(i)
avgDec = str(sumDec/len(stormsDec))

#write averages and data to new file in CSV format
averageData = open("hurricanes-updated.csv", "w")#Open a file for writing
averageData.write("Month,Average,2005,2006,2007,2008,2009,2010\n")
averageData.write("May" + "," + avgMay + ',' + stormsMay[0] + ',' + stormsMay[1] + ','
                  + stormsMay[2] + ',' + stormsMay[3] + ',' + stormsMay[4] + "," + stormsMay[5] + "\n")
averageData.write("Jun" + ","  + avgJune + ',' + stormsJune[0] + ',' + stormsJune[1] + ','
                  + stormsJune[2] + ',' + stormsJune[3] + ',' + stormsJune[4] + "," + stormsJune[5] + "\n")
averageData.write("Jul" + ","  + avgJuly + ',' + stormsJuly[0] + ',' + stormsJuly[1] + ','
                  + stormsJuly[2] + ',' + stormsJuly[3] + ',' + stormsJuly[4] + "," + stormsJuly[5] + "\n")
averageData.write("Aug" + ","  + avgAug + ',' + stormsAug[0] + ',' + stormsAug[1] + ','
                  + stormsAug[2] + ',' + stormsAug[3] + ',' + stormsAug[4] + "," + stormsAug[5] + "\n")
averageData.write("Sep" + ","  + avgSept+ ',' + stormsSept[0] + ',' + stormsSept[1] + ','
                  + stormsSept[2] + ',' + stormsSept[3] + ',' + stormsSept[4] + "," + stormsSept[5] + "\n")
averageData.write("Oct" + ","  + avgOct+ ',' + stormsOct[0] + ',' + stormsOct[1] + ','
                  + stormsOct[2] + ',' + stormsOct[3] + ',' + stormsOct[4] + "," + stormsOct[5] + "\n")
averageData.write("Nov" + ","  + avgNov+ ',' + stormsNov[0] + ',' + stormsNov[1] + ','
                  + stormsNov[2] + ',' + stormsNov[3] + ',' + stormsNov[4] + "," + stormsNov[5] + "\n")
averageData.write("Dec" + ","  + avgDec+ ',' + stormsDec[0] + ',' + stormsDec[1] + ','
                  + stormsDec[2] + ',' + stormsDec[3] + ',' + stormsDec[4] + "," + stormsDec[5] + "\n")

#close files
stormData.close()
averageData.close()
