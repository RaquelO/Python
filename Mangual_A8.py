#Raquel Mangual - Assignment #8 - Morse Code Translator

#create the morse code dictionary, last entry will insert two spaces between each word in the translation
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
