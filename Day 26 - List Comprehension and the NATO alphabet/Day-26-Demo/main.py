numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

new_range = [n * 2 for n in range(1, 5)]

strings = ["Alpha", "Beta", "Omega"]
new_strings = [n[0] for n in strings]

name = "Eoin"
letter_list = [letter for letter in name]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
long_caps = [name.upper() for name in names if len(name) >= 5]

print(long_caps)
