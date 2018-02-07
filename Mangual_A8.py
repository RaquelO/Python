#This program prompts the user to enter words or a phrase, then prints the user’s input translated into Morse code. 
#Uses periods for “dots” and hyphens for “dashes”. The program utilizes a dictionary for the conversion/translation.
#Places one space between each “letter” printed in Morse code; Places two spaces between each “word” printed in Morse code. 
#Uppercase and lowercase letters are treated equally.

#create the morse code dictionary as requied, add last entry that will insert two spaces between each word in the translation
morseCode = {"A":".-", "H":"....", "O":"---", "V":"...-",
             "B":"-...", "I":"..", "P":".--.", "W":".--",
             "C":"-.-.", "J":".---", "Q":"--.-", "X":"-..-",
             "D":"-..", "K":"-.-", "R":".-.", "Y":"-.--",
             "E":".", "L":".-..", "S":"...", "Z":"--..",
             "F":"..-.", "M":"--", "T":"-",
             "G":"--.", "N":"-.", "U":"..-", " ":"  "}

#prompt user for input and convert input to uppercase
message = input("Enter the message to be translated: ").upper()

#create a variable to save the translated message and initialize it with some text
translation = "The Morse code translation is: "

#check for input in data dictionary and append results to the translated message variable
for i in message :
    if i in morseCode :
        translation = translation + morseCode[i] + " "#add one space after each letter

#output the translation
print(translation)
