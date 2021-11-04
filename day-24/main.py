
# Closes the file automatically
with open("my_file.txt", mode="a+") as file:
    file.write("\nNew text")
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="a+") as file:
    file.write("\nNew file")

# Absolute path
with open("C:/Users/Hugo/Desktop/my_file.txt") as file:
    pass

# Relative path
with open("../../../../../../Desktop/my_file.txt") as file:
    pass

