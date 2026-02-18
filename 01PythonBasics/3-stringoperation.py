story = """
Once upon a time, there lived a crow in a hot, dry land.
The crow was extremely thirsty and searched everywhere for water.
After flying for hours, the crow spotted a pitcher with water at the bottom.
But the crow's beak was too short to reach the water.
The clever crow found small pebbles nearby and dropped them into the pitcher one by one.
As the pebbles accumulated, the water level rose gradually.
Finally, the water reached the top, and the crow could drink and quench its thirst.
The moral of the story: Little by little does the trick.
"""

print(story)

print(f"length of story is {len(story)} characters")

print(f"the word crow is found at {story.find('crow')} @ character position")

print(f"the word crow is found at {story.index('crow')} @ character position")

#write a code to replace crow with raven in the story and print the modified story
##string is immutable, so we cannot change it directly
story = story.replace("crow", "raven")  # replace 'crow' with 'raven'
print(story)

print(story.lower())  # convert string to lower case
print(story.upper())  # convert string to upper case

eachword = story.split()  # split the story into words
print(eachword)  # print the list of words
#print each word in the story on a new line
for word in eachword:
    print(word)