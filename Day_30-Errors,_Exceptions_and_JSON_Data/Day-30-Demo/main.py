# File not Found
# try:
#     file = open("file.txt")
#     dictionary = {"Key": "Value"}
#     value = dictionary["Key"]
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist in the dictionary")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File now closed")
#     raise TypeError("This is an error that I made up")

height = float(input("Height (Meters): "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 Meters")
bmi = weight / height ** 2
print(bmi)


# Index Error
# fruits = ["Apple", "Orange", "Grape"]
# fruit = fruits[3]

# Type Error
# text = "abc"
# print(text + 5)
