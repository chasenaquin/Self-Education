current_age = int(input("How old are you? "))
estimated_life_expectancy = int(input("At what age do you expect to die? "))

remaining_years = estimated_life_expectancy - current_age
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365


print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")


# #Angelas Code
# # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# years = 90 - int(age)
# months = round(years * 12)
# weeks = round(years * 52)
# days = round(years * 365)
#
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")
