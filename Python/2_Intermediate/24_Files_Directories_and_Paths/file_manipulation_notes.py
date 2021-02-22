# Open a file. (Default mode is read)
with open("test.txt", mode="r") as file:
    contents = file.read()
    print(contents)


# Dont use this method.
# file = open("test.txt")
# content = file.read()
# print(content)
# # Always remember to close files.
# file.close()

# Write to a file
# If opening with write mode, if file doesnt exist, this will create the file.
with open("test.txt", mode="w") as file:
    file.write("Write something to the file")

# Append to a file
with open("test.txt", mode="a") as file:
    file.write("Write something to the file")