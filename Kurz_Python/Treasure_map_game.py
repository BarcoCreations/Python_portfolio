
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


number = list(str(position))

if int(number[1]) == 3:
    if int(number[0]) == 1:
      row3[0] = "X"
    elif int(number[0]) == 2:
      row3[1] = "X"
    elif int(number[0]) == 3:
      row3[2] = "X"
elif int(number[1]) == 2:
    if int(number[0]) == 1:
      row2[0] = "X"
    elif int(number[0]) == 2:
      row2[1] = "X"
    elif int(number[0]) == 3:
      row2[2] = "X"
elif int(number[1]) == 1:
    if int(number[0]) == 1:
      row1[0] = "X"
    elif int(number[0]) == 2:
      row1[1] = "X"
    elif int(number[0]) == 3:
      row1[2] = "X"
else:
  print("Coordinate is out of range")


#second option
#horizontal = int(position[0])
#vertical = int(position[1])
#selected_row = map[vertical-1]
#selected_row[horizontal - 1] = "X"
#

print(f"{row1}\n{row2}\n{row3}")
