import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user == 0:
  user = rock
  print(rock)
elif user == 1:
  user = paper
  print(paper)
elif user == 2:
  user = scissors
  print(scissors)
else:
  print("You choose option out of range. You lose!")
choose = [rock, paper, scissors]
computer = random.choice(choose)
print(f"Computer chose:{computer}")

def compare(user, computer):
    if user == computer:
       return("It's A Tie :(....")
    elif user == rock:
         if computer == scissors:
             return("User Wins!")
         else:
             return("Computer Wins!")
    elif user == scissors:
         if computer == paper:
             return("User Wins!")
         else:
             return("Computer Wins!")
    elif user == paper:
         if computer == rock:
             return("User Wins!")
         else:
             return("Computer Wins!")

    else:
        return("User Choose Out Of The Options!")
        exit()
print(compare(user, computer))



