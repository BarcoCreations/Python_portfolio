
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowerCaseName1 = f"{name1}".lower()
lowerCaseName2 = f"{name2}".lower()

countT = lowerCaseName1.count("t")
countT += lowerCaseName2.count("t")
countR = lowerCaseName1.count("r")
countR += lowerCaseName2.count("r")
countU = lowerCaseName1.count("u")
countU += lowerCaseName2.count("u")
countE = lowerCaseName1.count("e")
countE += lowerCaseName2.count("e")
totalTrue = countT + countR + countU + countE

countL = lowerCaseName1.count("l")
countL += lowerCaseName2.count("l")
countO = lowerCaseName1.count("o")
countO += lowerCaseName2.count("o")
countV = lowerCaseName1.count("v")
countV += lowerCaseName2.count("v")
countE2 = lowerCaseName1.count("e")
countE2 += lowerCaseName2.count("e")
totalLove = countL + countO + countV + countE2

result = (str(totalTrue) + str(totalLove))
if int(result) < 10 or int(result) > 90:
  print(f"Your score is {result}, you go together like coke and mentos.")
elif int(result) > 40 and int(result) < 50:
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"Your score is {result}.")

wait = input("Press Enter to continue.")


import MainProgram