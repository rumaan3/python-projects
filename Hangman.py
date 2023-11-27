import random
import os 
import HangmanWords

print ("Welcome to Hangman!!!!")
chances = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#define a set of words and logic to pick a random word

def pick_word():

    word = random.choice(HangmanWords.word)
    print (word)
    return word

word = pick_word()
word = word.lower()

#once the word has been picked , create display of the number of letters in the word and
#according to the number of letters in the words , display underscores

display = []


# print (display)

for i in word:
    display.append(" _ ")
os.system('cls')   
print ("".join(display))
print("\n\n")
# take an input from the user to guess a letter
def pick_letter():
        letter = input ("\nInput a single letter which you think will be in this word\n")
        letter = letter.lower()
        return letter


def logic():
    
    for i in range(len(word)):
        if letter == word[i]:
            display[i] = letter

         
    return display




end = False

while not end:
    
    print( "welcome to hangman")
    
    if chances == 0:
        end = True
        print (f"You Lose!! The word was {word}")

    print (stages[chances])

    print(" ".join(display))
    
    if " _ " not in display:  
        end = True 
        print ("YOU WIN!!!!")
        break
    
    letter = pick_letter()
    logic()
       
    if letter not in word:
        chances -= 1
     








