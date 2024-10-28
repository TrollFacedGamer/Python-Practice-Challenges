
'''
Create a set of code that completes the following requirements:        A

The system should select a random number between 0-100.
The user should be able to guess four times, before revealing the answer.
The system should tell you if the guess is higher or lower than the actual number.,
Reminder: Insert comments, both a multi-line before the code and in-line comments.
'''

'''
Number guessing game
Generate number
'''
# import ranint
from random import randint
#
ran_num = randint(0, 100)

count = 0
while count < 4:
    ans = int(input("what is the number?"))
    if ans == ran_num:
        print("you got it right")
        break
    elif ans < ran_num:
        print("too low")
    elif ans > ran_num:
        print("too high")
    count += 1
    print("you have {0} chances left".format(4 - count))
print("you used up all of your chances")