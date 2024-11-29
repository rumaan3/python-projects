# phonetic alphabets and creating a list of words for each letter in an input word


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    # print(key,value)
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # print(index,row)
    # Access row.student or row.score
    # print(index,row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(data)

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
# print(data.to_dict())
x = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
y = input("Enter a Word : ")
result = []
for i in y:
    i = i.upper()
    result.append(x[i])

print(result)
