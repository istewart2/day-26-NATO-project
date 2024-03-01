import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("./nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_name = input("Enter your name: ").upper()
    try:
        phonetic_translation = [data_dict[letter] for letter in user_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_translation)


generate_phonetic()
