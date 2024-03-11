#Sophia Yang, 03/07/2024
#Mastermind Game
import random
secretCode = [str(random.randint(1, 9)), str(random.randint(1, 9)), str(random.randint(1, 9)), str(random.randint(1, 9))]
Guesses = [input("Enter your first guess: "), input("Enter your second guess: "), input("Enter your third guess: "), input("Enter your fourth guess: ")]
numGuesses = 1
print("Your guesses: " + str(Guesses))
def checkGuesses(codeMaker, codeBreaker):
	count = 0
	if (codeMaker[0] == codeBreaker[0]):
		count+=1
	if (codeMaker[1] == codeBreaker[1]):
		count+=1
	if (codeMaker[2] == codeBreaker[2]):
		count+=1
	if (codeMaker[3] == codeBreaker[3]):
		count+=1
	return count	
while(Guesses != secretCode):
	numCorrect = checkGuesses(secretCode, Guesses)
	print("You have " + str(numCorrect) + " guesses in the correct place.")
	Guesses.clear()
	Guesses.append(input("Enter your first guess: "))
	Guesses.append(input("Enter your second guess: "))
	Guesses.append(input("Enter your third guess: "))
	Guesses.append(input("Enter your fourth guess: "))
	print("Your guesses: " + str(Guesses))
	numGuesses += 1
print("Congratulations! You guessed all 4 numbers correct. It took you " + str(numGuesses) + " tries.")