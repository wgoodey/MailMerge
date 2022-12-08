NAMES_PATH = "./Input/Names/invited_names.txt"
LETTER_PATH = "./Input/Letters/starting_letter.txt"
OUTPUT_DIRECTORY = "./Output/ReadyToSend"


def process_names_list(list_path):
    with open(list_path) as file:
        name_list = file.read().splitlines()
        return name_list


def insert_name(recipient, text_path):
    with open(text_path) as file:
        letter_text = file.read()
        final_text = letter_text.replace("[name]", recipient)
        return final_text


def write_file(recipient, letter_text, output_directory):
    underscored_name = recipient.replace(' ', '_')
    with open(f"{output_directory}/{underscored_name}_letter.txt", "w") as file:
        file.write(letter_text)


def create_letter(recipient, letter_to_path, output_directory):
    letter = insert_name(recipient, letter_to_path)
    write_file(recipient, letter, output_directory)


# Using hardcoded file paths
# names = process_names_list(NAMES_PATH)
# for name in names:
#     create_letter(name, LETTER_PATH, OUTPUT_DIRECTORY)


# Using user input for file paths
names_path = input("What is the file path of the invite list?\n")
letter_path = input("What is the file path of the starting letter?\n")
output_directory_path = input("Where do you want to save the letters?\n")

names = process_names_list(names_path)

for name in names:
    create_letter(name, letter_path, output_directory_path)

print("Finished!")
