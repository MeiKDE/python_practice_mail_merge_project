# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"

with open(
    "/Users/mei/projects/python_practice_mail_merge_project/Input/Names/invited_names.txt",
    mode="r",
) as names_file:
    names = names_file.readlines()  # turn names into list
    # print(names)

# Step 1 : open starting_letter.txt
with open(
    "/Users/mei/projects/python_practice_mail_merge_project/Input/Letters/starting_letter.txt",
    mode="r",
) as letter_file:
    letter_content = letter_file.read()
    # Step 2: loop through names_file and replace the PLACEHOLDER value in the letter_file.
    for name in names:
        stripped_name = name.strip()  # to remove '\n' from the file
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        # Step 3: write letter into a new file(s)
        with open(
            f"/Users/mei/projects/python_practice_mail_merge_project/Output/ReadyToSend/letter_for_{stripped_name}.txt",
            mode="w",
        ) as completed_letter:
            completed_letter.write(new_letter)
