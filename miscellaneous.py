print("hi")


'''
python3 miscellaneous.py
Needs to be in one line
Runs the file

output: hi
'''

import sys
print(f"hi, {sys.argv[1]}")
'''
python3 miscellaneous.py john

output: hi john
'''

print(len(sys.argv))

'''
output: 2
'''

# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()