print("--++==[ Welcome to Python Pizza Deliveries! ]==++--")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("Selection was not valid.")

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1

print(price)



# # Angelas Code
#
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# bill = 0
# 
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25
#
# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
#
# if extra_cheese == "Y":
#   bill += 1
#
# print(f"Your final bill is: ${bill}.")
