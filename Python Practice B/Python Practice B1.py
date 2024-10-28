'''
Create a python program that will allow a user to input a certain amount of change, 
and then print how many quarters, dimes, nickels, 
and pennies are needed to make up the amount needed.
'''
# variable for amount of each coin
quarters = 0
dime = 0
nickels = 0
pennies = 0

#ask for change
change = float(input("How much change do you have?"))

#calculate amount of coin
while change >= 0.25:
    quarters += 1
    change -= 0.25
while change >= 0.10:
    dime += 1
    change -= 0.10
while change >= 0.05:
    nickels += 1
    change -= 0.05
while change > 0.01:
    pennies += 1
    change -= 0.01

#print coin
print(f"quarters: {quarters}")
print(f"dime: {dime}")
print(f"nickels: {nickels}")
print(f"pennies: {pennies}")
