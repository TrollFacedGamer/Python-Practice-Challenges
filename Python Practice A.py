'''
Create a set of code that completes the following requirements:        A

The system should select a random number between 0-100.
The user should be able to guess four times, before revealing the answer.
The system should tell you if the guess is higher or lower than the actual number.,
Reminder: Insert comments, both a multi-line before the code and in-line comments.
'''

import random
ran_num = random.randint(0, 100)

count = 0
while count <= 4:
    ans = int(input("what is the number?"))
    if ans == ran_num:
        print("you got it right")
        break
    elif ans < ran_num:
        print("too low")
    elif ans > ran_num:
        print("too high")
    count += 1

'''
Create a set of code that completes the following requirements:        B

Create a list of five words.
Generate a random number that includes the five entities in the list.
Users can guess letters that may exist in the word.
If a user inputs the entire word, it should say they win.
Reminder: Insert comments, both a multi-line before the code and in-line comments.
'''

list_five_words = ["hi", "sub", "hello", "morning", "bonjour"]


'''
Create a set of code that completes the following requirements:        C

There should be instructions for the user to know the code’s purpose.
Allow a user to contribute to a list of groceries until there are only five items.
Have the system print out each of item in the list, after sorting it in alphabetical order.
Reminder: Insert comments, both a multi-line before the code and in-line comments.
'''