"""
Homework #5 - bank account program
created by Raquel Mangual
"""

#Open the files containing the deposits and withdrawals in read only mode
depositFile = open("Deposits.txt", "r")
withdrawalFile = open("Withdrawals.txt", "r")

#Declare separate variables for the totals of each file
totalDeposits = 0
totalWithdrawals = 0

#Read the amounts of each file, assign the totals to a variable, strip away any linefeed escape sequences
for line in depositFile :
    totalDeposits += float(line.rstrip("\n"))

for line in withdrawalFile :
    totalWithdrawals += float(line.rstrip("\n"))

print("This program will calculate a new balance based on a starting balance and transactions saved in a file.")
while True :
    try :
        balance = input("Enter your starting balance: ")#prompt user to enter a starting balance and assign to a variable
        userBal = float(balance)#change value to float format
    except ValueError :#valide user's input
        print("Invalid input. Please enter a valid starting balance.")
    else :
        break

#calculate new balance by adding total deposits and withdrawals to user provided balance
newBal = format(userBal + totalDeposits - totalWithdrawals, ",.2f")
#output the new balance
print("Your ending balance is $", newBal)

#Close the file readivng variables
depositFile.close()
withdrawalFile.close()
