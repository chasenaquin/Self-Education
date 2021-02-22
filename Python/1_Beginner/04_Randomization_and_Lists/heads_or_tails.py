import random

coin = ["Heads", "Tails"]
print(random.choice(coin))

#If i cant use random.choice()
side = random.randint(0, 1)

if side == 0:
    print("Heads")
else:
    print("Tails")



# Angelas Code
# import random
#
# random_side = random.randint(0, 1)
# if random_side == 1:
#   print("Heads")
# else:
#   print("Tails")
