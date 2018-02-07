"""
This graphical program allows the user to enter an amount for a bill, select a tip percentage
and calculate the total amount due including the tip.
"""

#Import the tkinter module
import tkinter

#Main Function
def main() :
        #Creates the window
	test_window = tkinter.Tk()

	#Sets the window's title
	test_window.wm_title("Tip Calculator")

	#Creates three frames (all belong to test_window)
	upper_frame = tkinter.Frame(test_window)
	middle_frame = tkinter.Frame(test_window)
	lower_frame = tkinter.Frame(test_window)

        #Creates label, StringVar variable and entry field for bill amount
	billLabel = tkinter.Label(upper_frame, text="Enter the bill amount: ")
	global billAmountText
	billAmountText = tkinter.StringVar()
	billAmountText.set("")
	global billAmount
	billAmount = tkinter.Entry(upper_frame, width=10, textvariable=billAmountText)

	#Creates label for sliding scale, sliding scale to select tip amount and label for total bill
	tipLabel = tkinter.Label(middle_frame, text="Tip Amount (%):")
	global tipScale
	tipScale = tkinter.Scale(middle_frame, from_=0, to=50, tickinterval=10, orient="horizontal")
	tipScale.set(30)
	global totalLabelText
	totalLabelText = tkinter.StringVar()
	totalLabelText.set("Total Amount:")
	totalLabel = tkinter.Label(middle_frame, textvariable=totalLabelText)

	#Creates calculate, reset and quit buttons that belong to bottom frame
	calculateButton = tkinter.Button(lower_frame, text="Calculate Tip", command=calculateTotal)
	resetButton = tkinter.Button(lower_frame, text="Reset", command=resetNow)
	quitButton = tkinter.Button(lower_frame, text="Quit", command=test_window.destroy)

        #Pack all labels and fields onto their respective frames
	billLabel.pack()
	billAmount.pack()
	tipLabel.pack()
	tipScale.pack()
	totalLabel.pack()
	calculateButton.pack(side="left")
	resetButton.pack(side="left")
	quitButton.pack(side="left")

	#Pack each of the frames to the window
	upper_frame.pack()
	middle_frame.pack()
	lower_frame.pack()

        #Enters the main loop, displaying the window and waiting for events
	tkinter.mainloop()

#Function that calculates total amount due including tip
def calculateTotal() :
    totalBill = (str(float((tipScale.get()/100)+1)*float(billAmountText.get())))
    totalLabelText.set("Total Amount: " + totalBill)

#Function that resets the program
def resetNow() :
    billAmountText.set("")
    tipScale.set(30)
    totalLabelText.set("Total Amount: ")
    
#Calls the main function/starts the program	
main()
