
with open("./Input/Names/invited_names.txt", mode="r") as names:
    names_list = names.readlines()
    correct_names_list = []
    for name in names_list:
        x = name.strip("\n")
        correct_names_list.append(x)
    print(correct_names_list)

with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

for name in correct_names_list:
    new_letter = letter.replace("[name]", name)
    print(new_letter)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
        new_file.write(f"{new_letter}")