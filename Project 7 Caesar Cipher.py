logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
number = int(input("Type the shift number:\n"))
shift=number%26

def encrypt():
  word1=""
  for i in text:
    if i in alphabet:
      position=alphabet.index(i)
      letter=alphabet[(position+shift)%26]
      word1+=letter
    else:
      word1+=i
  print("Your message has been encrypted to:",word1)

def decrypt():
  word2=""
  for i in text:
    if i in alphabet:
      position=alphabet.index(i)
      letter=alphabet[(position-shift)%26]
      word2+=letter
    else:
      word2+=i
  print("Your message has been decrypted to:",word2)

if direction == "encode":
  encrypt()
elif direction == "decode":
  decrypt()
else:
  print("Please type 'encode' or 'decode'")

carry_on=input("do you want to continue,yes or no?").lower()

while(carry_on=="yes"):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if direction == "encode":
    encrypt()
  elif direction == "decode":
    decrypt()
  else:
    print("Please type 'encode' or 'decode'")

  carry_on=input("do you want to continue,yes or no?").lower()

print("Thank you for using the Caesar Cipher")
  