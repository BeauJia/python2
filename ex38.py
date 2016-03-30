# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
# split ten_things to ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']
# print stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop() # pop: more_stuff[-1]
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # stuff[-1]: the last one of stuff list.
print stuff.pop()
print ' '.join(stuff) # using blank space to joint stuff list. 
print '#'.join(stuff[3:5])
# using '#' to joint stuff[3]:Telephone and stuff[4]:Light. 

