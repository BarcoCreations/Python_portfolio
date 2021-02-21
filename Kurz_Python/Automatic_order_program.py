

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

peperoni_S_Price = 3
peperoni_ML_Price = 3
extra_Cheese_Price = 1
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
if size == "S":
  total_price = small_pizza_price
  if add_pepperoni == "Y":
    total_price += peperoni_S_Price
  if extra_cheese == "Y":
      total_price += extra_Cheese_Price
elif size == "M":
  total_price = medium_pizza_price
  if add_pepperoni == "Y":
    total_price += peperoni_ML_Price
  if extra_cheese == "Y":
    total_price += extra_Cheese_Price
elif size == "L":
  total_price = large_pizza_price
  if add_pepperoni == "Y":
    total_price += peperoni_ML_Price
  if extra_cheese == "Y":
    total_price += extra_Cheese_Price

print("Your final bill is: $" + str(total_price) + ".")

wait = input("Press Enter to continue.")

import MainProgram