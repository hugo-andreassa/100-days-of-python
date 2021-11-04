import pandas

# TODO 1. Create a dictionary in this format:
nato_file_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
nato_dict = {row.letter: row.code for (index, row) in nato_file_data.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
