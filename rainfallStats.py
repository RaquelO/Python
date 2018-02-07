"""
This program prompts the user to enter rainfall amounts (in inches) for 12 months of one year. The values are stored into a list.
Using the list created, the program will print out:
• The total rainfall
• The average monthly rainfall (Rounded to two decimal places.)
• The month with the most rain
• The month with the least rain
If the user enters a negative number for a month, user is prompted to re-enter a non-negative value for the month.
"""

#create an empty list
rainfallAmounts = []

#prompt user for input 12 times
for i in range(0, 12) :
    rainfall = int(input("Enter the rainfall amount for month " + str(i+1) + " "))
    while rainfall < 0 :#validate input, keep prompting user until valid value is entered
      rainfall = int(input("Invalid value, please enter a positive value for the rainfall amount: "))
    rainfallAmounts.append(rainfall)

#print a blank line
print()

#calculate and output total rainfall for the 12 month period
totalRainfall = 0
for i in range(0, 12) :
    totalRainfall = int(totalRainfall + rainfallAmounts[i])
print("The total rainfall for the year is:", totalRainfall, "inches.")

#calculate and output the average rainfall
averageRainfall = totalRainfall/12
print("The average rainfall for the year is:", averageRainfall, "inches.")

#determine and output the month with the most amount of rain
maxIndex = rainfallAmounts.index(max(rainfallAmounts))
print("The month with the most rain was month", maxIndex + 1)

#determine and output the month with the least amount of rain
minIndex = rainfallAmounts.index(min(rainfallAmounts))
print("The month with the least rain was month", minIndex + 1)
