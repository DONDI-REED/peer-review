# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Dondi Reed>
# Creation Date: <02/12/2022>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2': #<===space/indentation error removed and retyped and error was fixed
        print('Which cave will you go into? (1 or 2)')
        cave = input() #<===space error/indentation removed and retyped and error was fixed
#	return caves
    return cave #<===typo in variable name removed s

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
#	time.sleep(3) <==sleep not the same as the others
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
#		print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!')  #<==missing parenthesis and space after print
playAgain = 'yes'

#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':#<===should be double equap signs for both equal signs
	displayIntro()
#   caveNumber = choosecave()
	caveNumber = chooseCave()#<===misspelled variable Cave wasnt capitalized
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
#   if playAgain == "no":
	if playAgain == "no" or playAgain == 'n':#<===missing option for "n"
#		print("Thanks for planing")<===	 misspelled playing
		print("Thanks for playing")
	
