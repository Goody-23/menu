# literal assignment

first = "Goodness"
last = "Ibikunle"

print (type(first))
print (type(first) == str)
print( isinstance(first, str))


# constructor function

pizza = str("pepperoni")
print (type(pizza))
print (type(pizza) == str)
print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like anime from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?                                         

I was just checking in.              
                                            All good?
                                            
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\n\nHey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods

print (first)
print (first.lower())
print (first.upper())
print (first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                "
multiline = "                       " + multiline 
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = "menu"



x = 10 
for i in range(x):
    print(i)


print("Goodness is a dumb ass nigga sometime but he really be on his grind and shit")