# Lab 7-3 The Dice Game
import random

# the main function
def main():
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'
    playerOne, playerTwo = inputNames()
    
    while endProgram == 'no':
        winnerName = 'NO NAME'
        p1number = 0
        p2number = 0
        
        winnerName = rollDice(playerOne, playerTwo)
        displayInfo(winnerName)
        
        endProgram = input('Do you want to end the program? (yes/no): ')

#this function gets the players names
def inputNames():
    playerOne = input("Enter Player One's name: ")
    playerTwo = input("Enter Player Two's name: ")
    return playerOne, playerTwo

#this function will get the random values
def rollDice(playerOne, playerTwo):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    
    if p1number > p2number:
        return playerOne
    elif p2number > p1number:
        return playerTwo
    else:
        return "TIE"

# this function display the winner
def displayInfo(winnerName):
    print("The winner is:", winnerName)

# calls main
main()
