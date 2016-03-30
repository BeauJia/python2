# -*- coding: utf-8 -*-
# create a mapping of state to abbrevviation.

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them.
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities.
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# print out some cities.
print '-' * 10
print "NY States has: ", cities['NY']
print "OR States has: ", cities['OR']
# ----------
# NY States has:  New York
# OR States has:  Portland

# print some states.
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
# ----------
# Michigan's abbreviation is:  MI
# Florida's abbreviation is:  FL

# do it by using the state then cities dict.
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]
# ----------
# Michigan has:  Detroit
# Florida has: Jacksonville

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
# ----------
# Michigan is abbreviated MI
# New York is abbreviated NY
# Florida is abbreviated FL
# Oregon is abbreviated OR

#print every city in state.
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
# ----------
# FL has the city Jacksonville
# CA has the city San Francisco
# MI has the city Detroit
# OR has the city Portland
# NY has the city New York

# now do both at the same time.
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
# ----------
# Michigan state is abbreviated MI and has city Detroit
# New York state is abbreviated NY and has city New York
# Florida state is abbreviated FL and has city Jacksonville
# Oregon state is abbreviated OR and has city Portland

print '-' * 10
# safely get a abbrevition by state that might not be there.
state = states.get('Texas') # False

if not state:
	print "Sorry, no Texas."

# get a city with a default calue.
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s." % city
# ----------
# Sorry, no Texas.
# The city for the state 'TX' is: Does Not Exist.

