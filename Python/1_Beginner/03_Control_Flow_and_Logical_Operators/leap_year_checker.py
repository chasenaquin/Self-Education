year = int(input("Which year do you want to check? "))

# on every year that is evenly divisible by 4
#**except** every year that is evenly divisible by 100
#**unless** the year is also evenly divisible by 400

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")



# # Angelas Code
#
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Refer to the flow chart here: https://bit.ly/36BjS2D
#
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
