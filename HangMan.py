import random
import os

def welcomeScreen():
    #welcome statement and options
    print("Hello and welcome to Hangman!\nHere are your options:")
    
    print ("1. Play Hangman\n2. See high scores\n3. Quit")

    #input for user to pick from menu
    menuSelection = input ()
    if menuSelection == '1':
        game()
    elif menuSelection == '2':
        displayScore()
    else:
        quit()

    
def randomWordPicker():
    #imports random words created by yours truly
    iFile = open("HangMan Words.txt", 'r')

    #read
    iFile = iFile.read()

    #selects random word form the file to be the secret word
    word = random.choice(iFile.split())
    word = word.lower()
    
    #returns word var
    return word


def game():
    #sets empty value
    maxScore = 0

    #makes variable equal module
    word = randomWordPicker()

    #creates variables with empty values
    correctGuesses = ''
    incorrectGuesses = ''

    #makes playAgain set to Y and games to 0
    playAgain = 'Y'
    gamesPlayed = 0

    #gives user 10 guesses
    guesses = 10

    #Good luck msg
    print("Here is your secret word. Good luck!")
    
    #while loop to see if the user has played less than 4 games and if playAgain equals Y
    while gamesPlayed <= 4 and playAgain == 'Y':
        #empty value
        displayWord = ''

        #for loop to find char in word and see if your guess equals what the random word is
        for char in word:
            if char in correctGuesses:
                displayWord = displayWord + char + ''
            else:
                displayWord = displayWord + '-'
        #print the updated displayWord
        print (displayWord)

        #If Lost
        if guesses <= 0:
            gamesPlayed = gamesPlayed + 1
            saveScore(False)
            print("You have no more guesses... You lose. /n")
            #max games played
            if gamesPlayed == 4:
                print ("You have reached the maximum number of games. Thanks for playing!\n")
                break
            #play again?
            playAgain = input("Play again? Y/N").upper()
            #reset game stats
            word = randomWordPicker()
            guesses = 10
            incorrectGuesses = ''
            correctGuesses = ''
            continue
        #If Won
        elif displayWord == word:
            gamesPlayed = gamesPlayed + 1
            print ("Congrats! You've won!")
            saveScore(True)
            #max games played
            if gamesPlayed == 4:
                print ("You have reached the maximum number of games. Thanks for playing!\n")
                break
            #play again?
            playAgain = input("Play again? Y/N").upper()
            #reset game stats
            word = randomWordPicker()
            guesses = 10
            incorrectGuesses = ''
            correctGuesses = ''
            continue

        #input for user to guess a letter or word
        print ('\n')
        guess = input(str(guesses) + " guesses left\nGuess your letter or word: ")
        
        #If you guess a letter you've already used
        if guess in correctGuesses:
            print("Oops, you've already guessed this")
            guesses = guesses - 1
        else:
            #add your correct guess to correctGuesses var
            if guess in word:
                correctGuesses = correctGuesses + guess
                
            #add your incorrect guess to incorrectGuesses var
            else:
                incorrectGuesses = incorrectGuesses + guess
                guesses = guesses - 1

            #print the correct and incorrect guesses entered by user
            print ("CORRECT: ", correctGuesses, "INCORRECT:", incorrectGuesses)
    #run
    welcomeScreen()
    
def saveScore(win):
    #empty value
    data = []

    #find if file is found
    if os.path.isfile("highscore.txt"):
        rFile = open("highscore.txt", 'r')
        data = rFile.readlines()
    #is user wins
    if win == True:
        data.append("WIN\n")
    #is user loses
    else:
        data.append("LOSS\n")

    #wirte all dis new data the highscore.txt
    oFile = open("highscore.txt", 'w')    
    oFile.writelines(data)    
    oFile.close()

    
def displayScore():
    #empty values for dayzzz
    wins = 0
    losses = 0

    #find if file is found
    if os.path.isfile("highscore.txt"):
        #open highscore.txt and rename to f
        with open("highscore.txt") as f:
            #create content to readlines of f (high score)
            content = f.readlines()
        #finds however many WIN and LOSS lines are in content
        for line in content:
            #for the the wins on each line, add a win to wins
            if "WIN" in line:
                wins = wins + 1
            #for the losses on each line, add a loss to losses
            elif "LOSS" in line:
                losses = losses + 1

        #shows how many games you've won/lost
        print ("\n")
        print ("You have won " + str(wins) + " game(s)")
        print ("You have lost " + str(losses) + " game(s)\n")

    #is no high schores, print this:
    else:
        print ("No high scores\n")
        
    #run after viewing highscores
    welcomeScreen()

    
def main():
    #run the main menu
    welcomeScreen()

main()
