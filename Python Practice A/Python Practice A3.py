'''
Create a set of code that completes the following requirements:        C

There should be instructions for the user to know the code’s purpose.
Allow a user to contribute to a list of groceries until there are only five items.
Have the system print out each of item in the list, after sorting it in alphabetical order.
Reminder: Insert comments, both a multi-line before the code and in-line comments.
'''

list_of_groceries = [] #groceries list

def groceries_print(): #groceries list printer
    print("Your currrent Groceries are:")
    if len(list_of_groceries) == 0: #check if groceries list is empty
        print("You have no Groceries")
    else:
        for grocery in list_of_groceries: #print out numbered groceries list
            print(f"{list_of_groceries.index(grocery) + 1}. {grocery}")


print("Welcome to Groceries.exe") #welcome

groceries_print() #tell user list is empty
while len(list_of_groceries) < 5: #ask user 5 time to add to list
    list_of_groceries.append(input("What would you like to add?"))
    groceries_print()

print("Your grocery list is done")
y_n = (input("Would you like a file copy?"))
if y_n.lower() == "yes":
    file = open("list_of_groceries.txt", "a")

