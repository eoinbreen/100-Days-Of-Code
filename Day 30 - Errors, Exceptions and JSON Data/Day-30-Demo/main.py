# File not Found
try:
    file = open("file.txt")
    dictionary = {"Key": "Value"}
    value = dictionary["Key"]
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist in the dictionary")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File now closed")


# Key Error
# dictionary = {"Key": "Value"}
# value = dictionary["Another Key"]

# Index Error
# fruits = ["Apple", "Orange", "Grape"]
# fruit = fruits[3]

# Type Error
# text = "abc"
# print(text + 5)
