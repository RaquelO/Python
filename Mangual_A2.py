#Program that prompts user for a month and year, outputs the number of days in the month
#Includes consideration for Leap years

#prompt the user for the month and year, assign to variables and convert to integer format
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year (greater than 1000): "))
if month > 12 or month < 1 : #validate user input for month
    print("The month you entered is outside of the acceptable range.")
    print("The program has ended.")
elif year <1000 : #validate user in put for year
    print("The year you entered is outside of the acceptable range.")
    print("The program has ended.")
else :
    leapYes = True
    leapCalc1 = ((year % 100) and (year % 400))
    leapCalc2 =  (not(year % 100) and (year % 4))
    if (leapYes == (leapCalc1 or leapCalc2)) and month == 2 : #determine if month is February on a leap year
        print("There are 29 days in February ",year)
    elif month == 1 :
        print("There are 31 days in January ",year)
    elif month == 2 :
        print("There are 28 days in February ",year)
    elif month == 3 :
        print("There are 31 days in March ",year)
    elif month == 4 :
        print("There are 30 days in April ",year)
    elif month == 5 :
        print("There are 31 days in May ",year)
    elif month == 6 :
        print("There are 30 days in June ",year)
    elif month == 7 :
        print("There are 31 days in July ",year)
    elif month == 8 :
        print("There are 31 days in August ",year)
    elif month == 9 :
        print("There are 30 days in September ",year)
    elif month == 10 :
        print("There are 31 days in October ",year)
    elif month == 11 :
        print("There are 30 days in November ",year)
    elif month == 12 :
        print("There are 31 days in December ",year)
