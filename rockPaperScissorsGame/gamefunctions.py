"""
Functions for a rock/paper/scissors game
"""

#function to generate computer's game choice
def getRPS () :
    import random
    #generate a random number between 1 and 3 and assign the number to a variable
    programPick = random.randint(1,3)
    #return computer's game choice depending on number generated
    if programPick == 1 :
        return "rock"
    elif programPick == 2 :
        return "paper"
    else :
        return "scissors"

#function to determine and output the winner of the game
def whoWon (programPick, userPick) :
    if userPick == programPick :
        return "Tie"
    elif userPick == "rock" and programPick == "paper" :
        return "Computer"
    elif userPick == "rock" and programPick == "scissors" :
        return "User"
    elif userPick == "paper" and programPick == "rock" :
        return "User"
    elif userPick == "paper" and programPick == "scissors" :
        return "Computer"
    elif userPick == "scissors" and programPick == "rock" :
        return "Computer"
    else :
        return "User"
    
    
