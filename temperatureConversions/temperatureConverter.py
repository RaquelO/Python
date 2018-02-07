#This program uses a class to create a program that can convert a Fahrenheit temperature to Celsius and Kelvin.

#import the Temperature class module
from converter import Temperature

def main() :
    #create an instance of the class
    tempTest = Temperature()

    #get input from the user and convert it to float type
    userTemp = float(input("Enter a temperature in Fahrenheit: "))

    #call setter function to set temperature equal to user input
    tempTest.settemperature(userTemp)

    #print the temperature in fahrenheit using a getter function, rounded to two decimal places
    print("The temperature in Fahrenheit is: ", format(tempTest.gettemperature(), ",.2f"))

    #print the temperature in celsius using a getter function, rounded to two decimal places
    print("The temperature in Celsius is: ", format(tempTest.tocelsius(), ",.2f"))

    #print the temperature in Kelvin using a getter function, rounded to two decimal places
    print("The temperature in Kelvin is: ", format(tempTest.tokelvin(), ",.2f"))

#call the main function
main()


