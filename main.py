import pandas

data = pandas.read_csv(
    "C:/Users/anshm/Documents/Python Projects/NATO Alphabet/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Invalid character found.")
        continue
    else:
        print(output_list)
        break
