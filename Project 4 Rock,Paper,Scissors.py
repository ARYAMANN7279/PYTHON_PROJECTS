import random
computer=random.choice(["rock","paper","scissors"])
name=input("Hello !what's your name? ")
person=input(f"What will you choose {name} rock,paper or scissors? ")
if(computer=="rock"):
  print("computer played rock")
  print("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)

elif(computer=="paper"):
  print("computer played paper")
  print("""
      _______
  ---'   ____)____
              ______)
              _______)
  ---.__________)
  """)

elif(computer=="scissors"):
  print("computer played scissors")
  print("""
      _______
  ---'   ____)____
              ______)
       __________)
  ---.__(___)
  """)

if(person=="rock"):
  print("You played rock")
  print("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)

elif(person=="paper"):
  print("You played paper")
  print("""
      _______
  ---'   ____)____
              ______)
              _______)
  ---.__________)
  """)

elif(person=="scissors"):
  print("You played scissors")
  print("""
      _______
  ---'   ____)____
              ______)
       __________)
  ---.__(___)
  """)


if(computer==person):
  print("ooh it got tied,play again")
elif(computer=="rock" and person=="paper"):
  print("Congoo! you won")
elif(computer=="paper" and person=="scissors"):
  print("Congoo! you won")
elif(computer=="scissors" and person=="rock"):
  print("Congoo! you won")
else:
  print("sorry you lost,play again")




