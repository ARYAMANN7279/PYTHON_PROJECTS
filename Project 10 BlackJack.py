import random
print("Welcome to BlackJack!")
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
play=input("Would you like to play? (y/n): ").lower()
score=0
while(play=='y'):
  bid=int(input("How much would you like to bid? (in dollars):"))
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  a=random.choice(cards)
  b=random.choice(cards)
  c=random.choice(cards)
  d=random.choice(cards)
  print(f"Your cards are {a} and {b}.")
  print(f"One of The dealer's cards is {c}")
  hit=input("Would you like to hit? (y/n): ").lower()
  if(hit=='n'):
    print(f"Your total is {a+b}.")
    print(f"The dealer's cards are {c} and {d} and his total is {c+d}")
    if(a+b>c+d):
      print("You win!")
      score=score+bid*2
      print(f"You now own ${score}")
    elif(a+b==c+d):
      print("It's a tie!")
      score=score
      print(f"You now own ${score}")
    else:
      print("You lose!")
      print("You now own $0")
    play=input("Would you like to play again? (y/n): ").lower()  
  elif(hit=='y'):
    e=random.choice(cards) 
    print(f"Your cards are {a} and {b} and {e}.")
    if(a+b+e>21):
      print(f"Your total is {a+b+e} and you lost!")
      score=score-bid
      print(f"You now own {score}")
      play=input("Would you like to play again? (y/n): ").lower()
    else:
      print(f"Your total is {a+b+e}.")
      print(f"The dealer's cards are {c} and {d} and his total is {c+d}")
      if(a+b+e>c+d):
        print("You win!")
        score=score+bid*2
        print(f"You now own ${score}")
      elif(a+b+e==c+d):
        print("It's a tie!")
        score=score
        print(f"You now own ${score}")
      else:
        print("You lose!")
        score=score-bid
        print(f"You now own {score}")
      play=input("Would you like to play again? (y/n): ").lower()    
print("Thanks for playing!")
print(f"You exited the casino with ${score}")            
  