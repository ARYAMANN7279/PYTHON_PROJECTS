logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
import random 

print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")
num = random.randint(1, 100)
mode = input("Choose a difficulty. Type 'easy' (e) or 'hard' (h): ").lower()
attempts=0
if mode == "e":
    attempts = 10
elif mode == 'h':
    attempts = 5

while attempts > 0:
  print(f"No. of attempts left is {attempts}")
  attempts -= 1
  guess = int(input("Enter your Guess: "))
  if guess > num:
    
    print("Go lower,Try again")
  elif guess < num:
  
    print("Go higher,Try again")
  else:
    print(f"You guessed it right, the number was {num}")
    break
if attempts==0:
  print(f"Sorry, you've run out of attempts. The correct number was {num}")
