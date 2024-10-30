'''
Create a set of code that completes the following requirements:        C

There should be instructions for the user to know the code’s purpose.
Allow a user to contribute to a list of groceries until there are only five items.
Have the system print out each of item in the list, after sorting it in alphabetical order.
Reminder: Insert comments, both a multi-line before the code and in-line comments.
'''

list_of_groceries = ["hi", "moring", "hello", "lol", "sub"] #groceries list

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

import os # import os
print("Your grocery list is done") #declare code run is near done
y_n = (input("Would you like a file copy?")) #ask if user want a file copy
if y_n.lower() == "yes": #check user response
    
    if os.path.exists("list_of_groceries.txt"): #if file exist
        print("Warning a preexisting list of groceries has being detected")
        override_y_n = input("Would you like to replace the preexisting list?")
        if override_y_n.lower() == "yes": #over ride yes
            os.remove("list_of_groceries.txt") #delete old file
            file = open("list_of_groceries.txt", "a")
    
            for grocery in list_of_groceries: #file out numbered groceries list
                file.write(f"{list_of_groceries.index(grocery) + 1}. {grocery} \n") #note the slash is backwards
            file.close()
        elif override_y_n.lower() == "no": #over ride no
            print("Thank you for using Groceries.exe")
    else: #if file don't exist
        file = open("list_of_groceries.txt", "a")

        for grocery in list_of_groceries: #file out numbered groceries list
                file.write(f"{list_of_groceries.index(grocery) + 1}. {grocery} \n") #note the slash is backwards
        file.close()
