#******************************************************************************#
#                                PROGRAM Rock, Paper, Scissors                 #
# 
# AUTHOR: <Claudius Christian>
# FSU MAIL NAME: <cc08g@my.fsu.edu>
# RECITATION SECTION NUMBER: <01>
# RECITATION INSTRUCTOR NAME: <Cassie Urmano>
# CGS 3035 - Spring 2013
# PROJECT NUMBER: 4 
# DUE DATE: Tuesday 3/26/2013
# PLATFORM: Windows OS / Python 3.3.0
#
#******************************************************************************#
#                                SUMMARY                                       #
# 
#
# In this game, two people simultaneously choose either rock, paper, or
# scissors. Whether or not a player wins depends not only on what he or
# she chooses but also on what his or her opponent chooses. Here
# are the rules:
#
# Paper covers rock, paper wins.
# Rock breaks scissors, rock wins.
# All matching combinations are ties.
# In this game, Player 1 will be the program user, and Player 2 will be
# the computer. Player 1 will use  
#
#******************************************************************************#
#                                INPUT                                         #
#
# Player 1 will use interactive input to choose a move (1, 2, 3).
#
# You must ask the user to enter a command, and a numeric value for the
# measurement they want to convert. For example, if they enter a 2 for the
# command, then you would ask them to enter the number of feet they wish to
# convert to meters.
#
#******************************************************************************#
#                                OUTPUT                                        #
#
# Be sure to print out informative messages at the beginning of the program
# run, including an output title, a description of the game and its rules,
# and a description of what will occur during the program run.
#
# After each play of the game, print out the following in clear format: the
# choices each player made (print both the number giving the choice, and
# the word which describes it), which player won the game (or indicate a tie),
# and the amount of money each player has left. At the end of the program run
# print out a summary giving the total number of games actually played, the
# total number of games each player won, the number of tied games, the
# percentage of games won by each player, and the identity of the overall
# winner.
#
#******************************************************************************#
#                                ASSUMPTIONS                                   #
#
# It is possible that the user may enter an invalid command.  Your program must
# check for this error, and ask the user to re-enter a value when necessary,
# until a valid data item is entered.

#******************************************************************************#
#                                Import Files                                  #

import random

#******************************************************************************#
#                                Constants                                     #

ROCK           = 1                 # stores the rock move                 
PAPER          = 2                 # stores the paper move                           
SCISSORS       = 3                 # stores the scissors move              
AMOUNT_WAGERED = 10                # stores the amount bet per game
MIN_DOLLARS    = 0                 # stores the min amount lost per player 
MAX_ROUNDS     = 20                # stores the maximim games that can be played
PLAYERONEWIN   = 1                 # stores the player one win code
PLAYERTWOWIN   = 2                 # stores the player two win code
DRAW           = 3                 # stores the draw win code
PLAYERBROKE    = 0                 # stores the player bankrupt code            

SPACER12       = "            "    # format spacing
SPACER10       = "          "      # format spacing
SPACER6        = "      "          # format spacing
SPACER5        = "     "           # format spacing
SPACER4        = "    "            # format spacing
SPACER3        = "   "             # format spacing
SPACER2        = "  "              # format spacing
SPACER1        = " "               # format spacing
                                                          
#******************************************************************************#
#                                Main Function                                 #
                                                     
def main ():                                          
                                                                      
    playerOneMove  = 0             # stores player one's move
    playerTwoMove  = 0             # stores player two's move
    numGameWonP1   = 0             # stores how many times player one wins
    numGameWonP2   = 0             # stores how many times player two wins
    numGamesTied   = 0             # stores how many times the players tied
    playerOneMoney = 100           # stores the starting money for player one
    playerTwoMoney = 100           # stores the starting money for player two
    gamesPlayed    = 0             # stores the game starting game counter
    winner         = 0             # stores the winner

    

    # print intro information
    printIntro()

    while(gamesPlayed != MAX_ROUNDS and playerOneMoney != PLAYERBROKE and
          playerTwoMoney != PLAYERBROKE ):
            
        # prompt the user to enter an integer
        print ("\nPlayer one your move choices are:")
        print ("1 Rock")
        print ("2 Paper")
        print ("3 Scissors\n")

        # read in player ones choice
        playerOneMove = int(input("Player one your choice is: "))

        # determines if the users input was valid
        while( playerOneMove < 1 or playerOneMove > 3 ):

            # print message telling the user the input was invalid
            print ("\nYou entered an invalid choice please try again\n")
            # read in player ones choice
            playerOneMove = int(input("Player one your choice is: "))

        # call player two move generator
        playerTwoMove = playerTwoRandomMove()

        # winner stores the find winner function
        winner = findWinner(playerOneMove,  playerTwoMove)

        #this counts the players games won, and how much money each player has
        if( winner == 1):
            numGameWonP1 = numGameWonP1 + 1
            playerOneMoney = playerOneMoney + 10
            playerTwoMoney = playerTwoMoney - 10
        elif( winner == 2 ):
            numGameWonP2 = numGameWonP2 + 1
            playerOneMoney = playerOneMoney - 10
            playerTwoMoney = playerTwoMoney + 10
        elif( winner == 3 ):
            numGameWonP1 = numGameWonP1 + 0
            numGameWonP2 = numGameWonP2 + 0
            numGamesTied = numGamesTied + 1
            playerOneMoney = playerOneMoney + 0
            playerTwoMoney = playerTwoMoney + 0
        else:
            print("error")

        # this calls the draw function which shows the result after ever move  
        draw( playerOneMove, playerTwoMove, playerOneMoney, playerTwoMoney )

        # this keeps track of all games played
        gamesPlayed = gamesPlayed + 1

    # this prints the final results of the gmaes    
    results( numGameWonP1, numGameWonP2, gamesPlayed, winner, numGamesTied,
             gamesPlayed )
    
#******************************************************************************#
#                                Print Intro Function                          #
#
# Description: prints a user welcome message, and how to play the game

def printIntro():

    print ("\n======================================================")
    print ("        Welcome to the Rock Scissors Paper Program      ")
    print ("======================================================\n")
                                                                            
    print ("You will play against a computer opponent. After each ")
    print ("player makes a move the each match will be compared as")
    print ("follows.\n")

    print ("Player 1      Player 2                   Results                 ")
    print ("________      ________      ___________________________________  ")
    print ("Rock          Paper         Paper covers Rock.    Player 2 wins! ")
    print ("Paper         Scissors      Scissors cut's Paper. Player 2 wins! ")
    print ("Scissors      Rock          Rock breaks Scissors. Player 2 wins! ")
    print ("--------      --------      A matching pair results in a tie!\n\n")

    print ("You are Player 1, and the computer is Player 2.  Player 2's moves")
    print ("are randomly chosen by the computer. Both players start with $100")
    print ("and the game is finished when either one player reaches $0 or    ")
    print ("there have been 3 matches played. The bet per match is $10.      ")


# end of def printIntro():




#******************************************************************************#
#                                Determine Player Two's Move Function          #
#
# Description: this function make a random move for the computer

def playerTwoRandomMove():
    
   # generates a random integer number in the range of 1 through 3
    number = random.randrange(1, 4)
    return (number)

# end of def playerTwoRandomMove():

#******************************************************************************#
#                                Move Results Function                         #
#
# Description: this function prints the output when both players choose the
# same move

def draw( oneMove, twoMove, oneMoney, twoMoney):

    # sets the move number to the equivalent word
    if( oneMove == ROCK ):
       oneGesture = 'Rock'
    elif( oneMove == PAPER ):
       oneGesture = 'Paper'
    elif( oneMove == SCISSORS ):
       oneGesture = 'Scissors'
    else:
        oneGesture = 'error'

    # sets the move number to the equivalent word   
    if( twoMove == ROCK ):
       twoGesture = 'Rock'
    elif( twoMove == PAPER ):
       twoGesture = 'Paper'
    elif( twoMove == SCISSORS ):
       twoGesture = 'Scissors'
    else:
        twoGesture = 'error'

    print ("\nThis Rounds Results are:\n")
    print ("   Player 1          Player 2                 P1's     P2's ")
    print ("Number  Action    Number  Action    Winner    Money    Money")
    print ("______  ______    ______  ______    ______    _____    _____")

#=====================
# player 1 is rock
#=====================
    if( (oneMove == ROCK) & (twoMove==SCISSORS) ):
        print(oneMove,SPACER5, oneGesture,SPACER4,twoMove,SPACER5,twoGesture,
              "Player 1",SPACER3,oneMoney,SPACER4,twoMoney)
    elif( (oneMove == ROCK) & (twoMove == PAPER) ):
        print(oneMove,SPACER5, oneGesture,SPACER4,twoMove,SPACER5,twoGesture,
              SPACER3, "Player 2",SPACER2,oneMoney,SPACER4,twoMoney)
    elif( (oneMove == ROCK) & (twoMove == ROCK) ):
        print(oneMove,SPACER5, oneGesture,SPACER4,twoMove,SPACER5,twoGesture,
              SPACER4, "Draw",SPACER4,oneMoney,SPACER4,twoMoney)
#=====================
# player 1 is scissors
#=====================
    elif( (oneMove == SCISSORS) & (twoMove==ROCK) ):
        print(oneMove,SPACER5, oneGesture,SPACER1,twoMove,SPACER5,twoGesture,
              SPACER3, "Player 2",SPACER2,oneMoney,SPACER4,twoMoney)
    elif( (oneMove == SCISSORS) & (twoMove==PAPER) ):
        print(oneMove,SPACER5, oneGesture,SPACER1,twoMove,SPACER4,twoGesture,
              SPACER3, "Player 1",SPACER2,oneMoney,SPACER4,twoMoney)
    elif( (oneMove == SCISSORS) & (twoMove==SCISSORS) ):
        print(oneMove,SPACER5, oneGesture,SPACER1,twoMove,SPACER3,twoGesture,
              SPACER1, "Draw",SPACER4,oneMoney,SPACER4,twoMoney)
#=====================
# player 1 is paper
#=====================
    elif( (oneMove == PAPER) & (twoMove==ROCK) ):
        print(oneMove,SPACER5, oneGesture,SPACER3,twoMove,SPACER5,twoGesture,
              SPACER3, "Player 1",SPACER3,oneMoney,SPACER4,twoMoney)
    elif( (oneMove == PAPER) & (twoMove==PAPER) ):
        print(oneMove,SPACER5, oneGesture,SPACER4,twoMove,SPACER4,twoGesture,
              SPACER3, "Draw",SPACER4,oneMoney,SPACER4,twoMoney)
    elif( (oneMove == PAPER) & (twoMove==SCISSORS) ):
        print(oneMove,SPACER5, oneGesture,SPACER3,twoMove,SPACER4,twoGesture,
              SPACER1, "Player 2",SPACER2,oneMoney,SPACER4,twoMoney)
    else:
        print("error")
        
# end of def draw( oneMove, twoMove, oneMoney, twoMoney):

#******************************************************************************#
#                                Find Winner Function                          #
#
# Description: this function determines who wins

def findWinner(oneMove, twoMove):

    whoWon = 0
    
    if( (oneMove == ROCK) & (twoMove==SCISSORS) ):
        whoWon = PLAYERONEWIN
    elif( (oneMove == SCISSORS) & (twoMove==PAPER) ):
        whoWon = PLAYERONEWIN
    elif( (oneMove == PAPER) & (twoMove==ROCK) ):
        whoWon = PLAYERONEWIN   
    elif( (oneMove == ROCK) & (twoMove == PAPER) ):
        whoWon = PLAYERTWOWIN
    elif( (oneMove == SCISSORS) & (twoMove==ROCK) ):
        whoWon = PLAYERTWOWIN
    elif( (oneMove == PAPER) & (twoMove==SCISSORS) ):
        whoWon = PLAYERTWOWIN
    else:
        whoWon = DRAW
    
    return whoWon

# end of def findWinner(oneMove, twoMove):
        
#******************************************************************************#
#                                Print Results Function                        #
#
# Description: this function prints the results of the games played

def results( totalP1Wins, totalP2Wins, totalGames, victor, totaGamesTied,
             totalGamesPlayed ):
    percentageP1Wins = (totalP1Wins / totalGames) * 100 
    percentageP2Wins = (totalP2Wins / totalGames) * 100 


    print ("\n\nThe final results for tonight's game are as follows:\n")
    print (SPACER12, "Player 1", SPACER5, "Player 2")
    print (SPACER12, "________", SPACER5, "________")
    print ("Games won:",SPACER5, totalP1Wins, SPACER10, totalP2Wins)
    print ('Percentage Won: %.1f' % percentageP1Wins, SPACER6,
           format(percentageP2Wins, '.1f'))

    print("\nTotal games played: ", totalGamesPlayed) 
    print("Total games tied: ", totaGamesTied)  
    print("Total player 1 wins:", totalP1Wins)
    print("Total player 2 wins:", totalP2Wins)

    # determines which player won the most and prints that the winningest player
    if( totalP1Wins > totalP2Wins ):
        print ("\nPlayer one is the champion.")
    elif ( totalP1Wins < totalP2Wins):
        print ("\nPlayer two is the champion.")
    elif( totalP1Wins == totalP2Wins):
        print ("\nThe players are tied")
    else:
        print ("\nerror")

# def results( totalP1Wins, totalP2Wins, totalGames, victor, totaGamesTied,
#              totalGamesPlayed ):        
 
main()

#******************************************************************************#
#                                E N D  P R O G R A M                          #
