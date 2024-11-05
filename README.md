# Mail Merge Project

This project automates the creation of personalized letters for a list of invited names. Using a starting letter template, the project replaces the `[name]` placeholder with each name from a list and saves each customized letter as a new file.

## Project Structure

- **invited_names.txt**: Contains a list of names, each on a new line, to be used in the letters.
- **starting_letter.txt**: The template letter with a placeholder `[name]` for each recipient’s name.
- **ReadyToSend**: The output folder where personalized letters will be saved.

## How It Works

1. **Read the Names**: Each name in `invited_names.txt` is read and stored as a list.
2. **Read the Template**: The template letter in `starting_letter.txt` is loaded with a `[name]` placeholder.
3. **Replace and Save**:
   - For each name, the placeholder `[name]` is replaced with the actual name.
   - A new letter file is generated and saved in the `ReadyToSend` folder.

## Code Overview

### PLACEHOLDER

The placeholder `[name]` is defined as a constant so it can be easily reused in the code.

### File Reading and Writing

- **Read `invited_names.txt`**: Reads each name as a list of strings.
- **Read `starting_letter.txt`**: Loads the template letter content.
- **Write Output**: For each name, replaces the placeholder with the name and writes the customized letter to a new file.
