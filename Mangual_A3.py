#prompt user for name and time of first competitor
comp1 = input("Enter the name of the first competitor: ")
time1 = int(input("Enter the finish time of the first competitor (greater than zero): "))

#validate finish time for first competitor
while time1 <= 0 :
    time1 = int(input("Time entered is invalid, please enter a valid finish time"))
else :#get info for second competitor once user enters valid input for first competitor
    comp2 = input("Enter the name of the second competitor: ") 
    time2 = int(input("Enter the finish time of the second competitor (greater than zero): "))
    while time2 <= 0 :
            time2 = int(input("Time entered is invalid, please enter a valid finish time"))
    else :#get info for third competitor once user enters valid input for second competitor
        comp3 = input("Enter the name of the third competitor: ") 
        time3 = int(input("Enter the finish time of the third competitor (greater than zero): "))
        while time3 <= 0 :
                time3 = int(input("Time entered is invalid, please enter a valid finish time"))
#determine and output who won which medal
if (time1 < time2) and (time2 < time3) : 
    print("Gold medal goes to",comp1)
    print("Silver medal goes to",comp2)
    print("Bronze medal goes to",comp3)
elif (time1 < time3) and (time3 < time2) : 
    print("Gold medal goes to",comp1)
    print("Silver medal goes to",comp3)
    print("Bronze medal goes to",comp2)
elif (time2 < time1) and (time1 < time3) : 
    print("Gold medal goes to",comp2)
    print("Silver medal goes to",comp1)
    print("Bronze medal goes to",comp3)
elif (time2 < time3) and (time3 < time1) : 
    print("Gold medal goes to",comp2)
    print("Silver medal goes to",comp3)
    print("Bronze medal goes to",comp1)
elif (time3 < time1) and (time1 < time2) : 
    print("Gold medal goes to",comp3)
    print("Silver medal goes to",comp1)
    print("Bronze medal goes to",comp2)
else : 
    print("Gold medal goes to",comp3)
    print("Silver medal goes to",comp2)
    print("Bronze medal goes to",comp1)
