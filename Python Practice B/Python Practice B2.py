'''
Create a Mad Libs-style game, 
where the program asks the user for certain types of words, 
and then prints out a story with the words that the user input. 
The story doesn't have to be too long, 
but it should have some sort of storyline.

a. Output the resulting story into a text file
'''

'''
Story Template

[name] when a walk in [month] to the [destination]. [name] got lost in [city] and took [days] days to get to [destination]
'''

#story generator
def story(name, month, destination, city, days):
    #sentence generator
    sentence_1 = "{0} when a walk in {1} to the {2}.".format(name, month, destination)
    sentence_2 = "{0} got lost in {1} and took {2} days to get to {3}".format(name, city, days, destination)
    
    #sentence combiner
    return sentence_1 + " " + sentence_2 + "."

text_file = open("text_file", "w")

text_file.write(story(input("Name: "), input("Month: "), input("Destination: "), input("City: "), input("Number of Days: ")))

