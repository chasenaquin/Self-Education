height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / (height ** 2)

print(f"Your BMI is: {BMI}")


# #Angelas Code
#
# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# weight_as_int = int(weight)
# height_as_float = float(height)
#
# # Using the exponent operator **
# bmi = weight_as_int / height_as_float ** 2
# # or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)
#
# bmi_as_int = int(bmi)
#
# print(bmi_as_int)
