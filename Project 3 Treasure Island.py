print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/__
*******************************************************************************''')


name=input("Ahoy! mate\nWhat is your name? ")
print(f"Welcome to the Treasure Island {name}.\nYour mission is to find the treasure. ")
choice_1=input(f"Where do you wanna go {name} left or right ").lower()
if(choice_1=='left'):
  choice_2=input("You have reached the shore,do you wanna swim or wait for a boat ").lower()
  if(choice_2=='wait'):
    choice_3=input("You have reached the gates of the dragons,which door do you choose red,blue or yellow ").lower()
    if(choice_3=='yellow'):
      print(f"Good job {name}!!! You reached the treasure ")
    elif(choice_3=='red'):
      print("OH lord,you were burned by fire.GAME OVER")
    elif(choice_3=='blue'):
      print("Holy cow! The dragons ate you.GAME OVER")
    else:
      print("GAME OVER")
  else:
    print("Oh damn. You were attacked by a crocodile monster.GAME OVER")
else:
  print("Oh shikes!You fell into a hole.GAME OVER")
    