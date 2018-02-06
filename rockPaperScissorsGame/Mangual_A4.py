"""
This is a game of rock, paper, scissors where the user plays against the program.
I created a module to randomly select the program's choice against the player, and to determine the winner of a round.
"""

#Import the gamefunctions module
import gamefunctions

def main() :
  playAgain = "yes"#control variable for/if when user wants to play game again
  while playAgain == "yes" :
  #Prompt the user to enter their game choice and validate user input
    print("Lets play a game of rock, paper, scissors")
    userPick = input("Enter your choice (rock, paper or scissors) in lowercase: ")
    while userPick != "rock" and userPick != "paper" and userPick!= "scissors" :
      userPick = input("Invalid choice, please enter rock, paper or scissors: ")
    else :  
    #get the computer's game choice
      programPick = gamefunctions.getRPS()
    #Pass user's choice and computer's choice to whoWon function
      winner = gamefunctions.whoWon(programPick, userPick)
      if winner == "Tie" :
        print("The computer chose", programPick)
        print("Tie!")
      elif winner == "User" :
        print("The computer chose", programPick)
        print("You win!")
      else :
        print("The computer chose", programPick)
        print("Computer wins!")
    #ask user if they want to play again or end the game, and validate user input
    playAgain = input("Would you like to play again? Enter yes or no ")
    while playAgain != "yes" and playAgain != "no" :
        playAgain = input("Invalid choice, please enter yes or no: ")
    else :
        playAgain = playAgain.lower()
  else :
    print("Game over, thanks for playing")

#Calls main function
main()
