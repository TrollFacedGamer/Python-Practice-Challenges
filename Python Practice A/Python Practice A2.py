'''
Create a set of code that completes the following requirements:        B

Create a list of five words.
Generate a random number that includes the five entities in the list.
Users can guess letters that may exist in the word.
If a user inputs the entire word, it should say they win.
Reminder: Insert comments, both a multi-line before the code and in-line comments.
'''

from random import randint

list_five_words = ["hi", "sub", "hello", "morning", "bonjour"]
num = randint(0, 4)

while True:
    lettter_word = input("Guess the word. No caps:")
    if lettter_word == list_five_words[num]:
        print("You win")
        break
    elif lettter_word in list_five_words[num]:
        print("Not quite, but {0} is in the word".format(lettter_word))
    else:
        print("wrong")