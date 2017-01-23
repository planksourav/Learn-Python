# Assign the value of all attributes
people = 30
cars = 40
buses = 15

#First logic between cars and people
if cars > people:
    print "We should take the cars."
elif cars > people:
    print "We should not take cars."
else:
    print " We can't decide."
# Second logic between bus and car
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."
# Third logic between people and buses
if people > buses:
    print "Alright, let's just take the buses."
else:
    print " Fine, Let's stay home then."