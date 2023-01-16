with open("new_file.txt", mode="w") as file:  # Write Mode. Creates file if it does not exist, ONLY CREATES ON WRITE
    file.write("New Text")

with open("new_file.txt", mode="a") as file:  # Append Mode
    contents = file.write("\nAnother New Line")

with open("new_file.txt", mode="r") as file:  # Read Mode
    contents = file.read()
    print(contents)

with open("../../Day 20 & 21 - Animation, Inheritance and List Slicing/Snake-Game/high_score.txt", mode="r") as file:  # Relative Location
    contents = file.read()
    print(f"The High Score in the Snake Game is {contents}")
