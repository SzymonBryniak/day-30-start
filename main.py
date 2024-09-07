# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

while True:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    except KeyError as Val_Entered:
        print(f"illegal word {Val_Entered} was entered")
        continue


# Udemy version
# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#         generate_phonetic()
#     else:
#         print(output_list)
#
#
# generate_phonetic()
