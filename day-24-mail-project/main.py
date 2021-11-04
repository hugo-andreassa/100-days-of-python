
letter_text = ""
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_text = letter_file.read()
    # print(letter_text)

invited_names = []
with open("./Input/Names/invited_names.txt") as names_file:
    content = names_file.read()
    invited_names =+ content.split("\n")
    # print(invited_names)

finished_letters = []
for name in invited_names:
    finished_letter_text = letter_text.replace("[name]", name)
    finished_letters.append((name, finished_letter_text))

for letter in finished_letters:
    letter_name = letter[0]
    letter_text = letter[1]
    with open(f"./Output/ReadyToSend/letter_for_{letter_name}", "w") as file:
        file.write(letter_text)
