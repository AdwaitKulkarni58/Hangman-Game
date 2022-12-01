import random

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

word_list = ["aardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, len(word_list) - 1)]

lives = 6

display = []
for letter in chosen_word:
  display.append("_")

while True:
  if "_" not in display:
    print("You win.")
    break
  user_input = input("Guess a letter:")
  guess = user_input.lower()
    
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if (letter == guess):
      display[position] = letter
  
  print("".join(display))
  
  if guess not in display:
    lives = lives - 1
    if (lives == 0):
      print(stages[0])
      print("You lose")
      break
  print(stages[lives])