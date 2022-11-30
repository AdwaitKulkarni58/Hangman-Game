import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, len(word_list) - 1)]

user_input = input("Guess a letter:")
guess = user_input.lower()

for letter in chosen_word:
  if (letter == guess):
    print("right")
  else:
    print("wrong")