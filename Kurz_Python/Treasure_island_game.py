print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome Melichar to Treasure Island.")
print("Melichar! Your mission is to find the treasure.") 

print("You are at a cross road. Where do you want to go? Type left or right: ")
direction = input().lower()


if direction == "left":
  print('You\'re come to a lake. There is a island in the middle of the lake. Type wait for a wait for a boat. Type a swim to swim across\n')
  direction = input().lower()
  if direction == "wait":
    print("You arrive at the island unharmed. There is house with three doors. One red, one yellow and one blue. Which color you do choose?")
    direction = input().lower()
    if direction == "red":
     print("Burned by fire. Game Over.")
    elif direction == "yellow":
     print("You Win!")
    elif direction == "blue":
     print("Eaten by beasts. Game Over")
    else:
     print("Game Over. Nataly :(")
  else:
   print("Attacked by troat and fog. Game Over.")
else:
  print("Melichar! You are fall into a hole. Game Over.")


wait = input("Press Enter to continue.")

import MainProgram