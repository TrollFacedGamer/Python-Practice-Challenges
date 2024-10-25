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
