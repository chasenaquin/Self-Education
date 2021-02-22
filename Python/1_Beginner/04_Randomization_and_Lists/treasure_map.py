row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Use 22
y_axis = position[0]
x_axis = position[1]

map[int(y_axis) - 1][int(x_axis) - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# #Angelas Code
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where do you want to put the treasure? ")
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# map[vertical - 1][horizontal - 1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")
