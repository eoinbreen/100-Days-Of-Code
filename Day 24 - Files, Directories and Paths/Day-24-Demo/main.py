with open("new_file.txt", mode="w") as file:  # Write Mode. Creates file if it does not exist, ONLY CREATES ON WRITE
    file.write("New Text")

with open("new_file.txt", mode="a") as file:  # Append Mode
    contents = file.write("\nAnother New Line")

with open("new_file.txt", mode="r") as file:  # Read Mode
    contents = file.read()
    print(contents)