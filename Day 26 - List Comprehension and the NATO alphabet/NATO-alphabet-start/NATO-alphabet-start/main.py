import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_codes = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("What is your name? ").upper
nato_name = [nato_codes[letter] for letter in user_name]
print(nato_name)
