def prime_number_checker(number):
    is_prime = True
    #Resulting in the absence of "1" and "number itself".
    for position in range(2, number):
        if number % position == 0:
            is_prime = False

    print(f"Prime Number: {is_prime}")

n = int(input("Check this number: "))
prime_number_checker(number=n)


#Prime numbers can only be divided by 1 and itself


# #Angelas Code
# #Write your code below this line 👇
#
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
# #Write your code above this line 👆
#
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)
