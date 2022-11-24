#guessing game
import random

guesses_left = 3
solution = random.randint(1,10)

while guesses_left != 0:
  guess = int(input(f"Guess a number between 1 and 10. You have {guesses_left} guesses remaining: "))

  if guess == solution:
    print("Congratulations! You guessed it!")
    break
  
  guesses_left -=1

#last break if condition is over
else:
  print("Sorry, out of guesses. you lose.")  

print("Game Over!")