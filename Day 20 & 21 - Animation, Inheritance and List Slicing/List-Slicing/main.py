piano_keys = ["a", "b", "c", "d", "e", "f", "g", "h"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[1:])  # Takes out first value
print(piano_keys[::-1])  # Reverses
print(piano_keys[1:len(piano_keys):2])  # only prints every 2nd one
print(piano_tuple[0:-1])  # Takes out final value - stops before value
