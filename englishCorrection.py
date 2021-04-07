# Done By Omar Rahwanji ^_^
from textblob.en import Spelling
import re  # Regular Expression Module


# ===========================Training================================

def train():
    with open("dataset.txt", encoding="utf8") as f1:  # Open our source file
        text = f1.read()  # Read the file
        text_to_lower = text.lower()  # Lower all the capital letters

    words = re.findall("[a-z]+", text_to_lower)  # Find all the words and place them into a list
    one_string = " ".join(words)  # Join them into one string

    path_to_file = "train.txt"  # The path we want to store our stats file at
    spelling = Spelling(path=path_to_file)  # Connect the path to the Spelling object
    spelling.train(one_string, path_to_file)  # Train
    print('Successfully Trained!')
    return 0


# ===================================================================

# ========================Correction Method==========================

def correct(txt):
    path_to_file = "train.txt"
    spelling = Spelling(path=path_to_file)
    text = txt.lower()
    words = text.split()
    corrected = ""
    for i in words:
        corrected = corrected + " " + spelling.suggest(i)[0][0]  # Spell checking word by word
    corrected = corrected.strip()
    return corrected


# ===================================================================
