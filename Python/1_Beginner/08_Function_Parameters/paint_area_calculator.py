import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((test_h * test_w) / coverage)
    print(f"Number of cans: {number_of_cans}")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



# # Angelas Code
# #Write your code below this line 👇
# import math
#
# def paint_calc(height, width, cover):
#     num_cans = (height * width) / cover
#     round_up_cans = math.ceil(num_cans)
#     print(f"You'll need {round_up_cans} cans of paint.")
#
# #Write your code above this line 👆
#
#
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
